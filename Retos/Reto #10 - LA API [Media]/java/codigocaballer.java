import java.io.File;
import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpRequest.BodyPublisher;
import java.net.http.HttpResponse;
import java.nio.file.Files;
import java.util.ArrayList;
import java.util.Base64;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

import javax.swing.JFileChooser;

import com.google.gson.Gson;

import lombok.AccessLevel;
import lombok.Getter;

/*
 * Tested with 
 *  JavaSE-11
 *  gson-2.8.5
 *  lombok-1.18.24
 */


/*
 * Base class to manage api responses
 */
abstract class Response {
    @Getter
    protected String resource;
    protected int response_code;

    public int getResponseCode() {
        return response_code;
    }
}

/**
 * Class to deserialize a Scan Request
 */
final class ScanResponse extends Response {
    private final String verbose_msg;

    public ScanResponse(String resource, int response_code, String verbose_msg) {
        this.resource = resource;
        this.response_code = response_code;
        this.verbose_msg = verbose_msg;
    }

    public String getVerboseMsg() {
        return verbose_msg;
    }

    @Override
    public String toString() {
        return "{" +
                " resource='" + this.getResource() + "'" +
                ", response_code='" + this.getResponseCode() + "'" +
                ", verbose_msg='" + this.getVerboseMsg() + "'" +
                "}";
    }
}

/**
 * This is a helper class to deserialize the scan result
 */
@Getter
class Scan {
    private final boolean detected;
    private final String version;

    public Scan(boolean detected, String version) {
        this.detected = detected;
        this.version = version;
    }
}

/**
 * Class to deserialize a Report Request
 */
@Getter
final class ReportResponse extends Response {
    private final int total;
    private final int positive;
    @Getter(AccessLevel.NONE)
    private final String verbose_msg;
    private final Map<String, Scan> scans;

    public ReportResponse(String resource, int response_code, int total, int positive, String verbose_msg,
            Map<String, Scan> scans) {
        this.resource = resource;
        this.response_code = response_code;
        this.total = total;
        this.positive = positive;
        this.verbose_msg = verbose_msg;
        this.scans = scans;
    }

    public String getVerboseMsg() {
        return verbose_msg;
    }

    @Override
    public String toString() {
        return "{" +
                " resource='" + getResource() + "'" +
                ", response_code='" + getResponseCode() + "'" +
                ", total='" + getTotal() + "'" +
                ", positive='" + getPositive() + "'" +
                ", verbose_msg='" + getVerboseMsg() + "'" +
                "}";
    }
}

/**
 * Class to save every uri or body param better than a map<string, object>
 */
class NetworkParam {
    private String name;
    private Object value;

    public NetworkParam(String name, Object value) {
        this.name = name;
        this.value = value;
    }

    public String getName() {
        return name;
    }

    public Object getValue() {
        return value;
    }
}

/**
 * Class to manage requests and responses to the VirusTotal pubic API
 */
class VirusTotalApi {
    private static final String BASE_URI = "https://www.virustotal.com/vtapi/v2/";
    private static final String SCAN_URI = BASE_URI + "file/scan";
    private static final String REPORT_URI = BASE_URI + "file/report";

    private static final String API_KEY = "PASTE_YOUR_API_KEY_HERE";

    private static String getReportUri(List<NetworkParam> params) {
        params.add(0, new NetworkParam("apikey", API_KEY));
        String paramsString = buildBodyAndUrlParams(params);
        return REPORT_URI + "?" + paramsString;
    }

    private static String buildBodyAndUrlParams(List<NetworkParam> params) {
        String paramsString = params
                .stream()
                .map(e -> e.getName() + "=" + e.getValue())
                .collect(Collectors.joining("&"));
        return paramsString;
    }

    public static ScanResponse makeScanRequest(File file, List<NetworkParam> params) throws Exception {
        Map<String, String> headers = new HashMap<String, String>() {
            {
                put("accept", "text/plain");
                put("content-type", "application/x-www-form-urlencoded");
            }
        };

        String uri = SCAN_URI + "?apikey="
                + API_KEY;
        String bodyString = buildBodyAndUrlParams(params);
        BodyPublisher bodyPublisher = HttpRequest.BodyPublishers.ofString(bodyString);
        String responseBody = NetworkUtils.makeHttpRequest(uri,
                headers, "POST", bodyPublisher);

        Gson gson = new Gson();
        final ScanResponse response = gson.fromJson(responseBody, ScanResponse.class);
        return response;
    }

    public static ReportResponse makeReportRequest(String resource) throws Exception {
        List<NetworkParam> paramsReport = new ArrayList<>();
        paramsReport.add(new NetworkParam("resource",
                resource));
        paramsReport.add(new NetworkParam("allinfo", false));

        String uri = getReportUri(paramsReport);
        BodyPublisher bodyPublisher = HttpRequest.BodyPublishers.noBody();
        String responseBody2 = NetworkUtils
                .makeHttpRequest(uri, null, "GET", bodyPublisher);

        Gson gson = new Gson();
        final ReportResponse reportReponse = gson.fromJson(responseBody2, ReportResponse.class);
        return reportReponse;
    }
}

/**
 * Every api operation
 */
class VirusTotalApiOperation {
    public static final int RESPONSE_NOT_FOUND = 0;
    public static final int RESPONSE_OK = 1;
    public static final int RESPONSE_IN_QUEUE = -2;

    public static ScanResponse launchFileScan() throws Exception {
        File sample = FileUtils.launchFileChooser();
        System.out.println("Launching scan request");
        List<NetworkParam> params = new ArrayList<>();
        params.add(new NetworkParam("file", sample));

        final ScanResponse vtResponse = VirusTotalApi.makeScanRequest(sample, params);
        System.out.println("Response code " + vtResponse.getResponseCode());
        System.out.println(vtResponse.getVerboseMsg());
        manageResponse(vtResponse);
        System.out.println();
        return vtResponse;
    }

    public static void printScanReport(ReportResponse reportReponse) {
        System.out.println("VirusTotal Report Response: " + reportReponse.getVerboseMsg() +
                "\n");

        Map<String, Scan> scans = reportReponse.getScans();
        if (scans instanceof Map) {
            System.out.println("Positives: " + reportReponse.getPositive() + "/" + reportReponse.getTotal());
            Map<String, Scan> positives = scans.entrySet().stream()
                    .filter(scan -> scan.getValue().isDetected())
                    .collect(Collectors.toMap(scan -> scan.getKey(), scan -> scan.getValue()));
            if (!positives.isEmpty()) {
                System.out.println("Resume of positive detections:");

                for (Map.Entry<String, Scan> scan : positives.entrySet()) {
                    System.out.println(
                            "\t" + scan.getKey() + "\t Version " + scan.getValue().getVersion());
                }
            }
        }
    }

    public static ReportResponse launchFileReport(String resource) throws Exception {
        System.out.println("Launching report request to resource " + resource + "*");
        final ReportResponse reportReponse = VirusTotalApi.makeReportRequest(resource);
        System.out.println("Response code " + reportReponse.getResponseCode());
        printScanReport(reportReponse);
        return reportReponse;
    }

    private static void manageResponse(Response response) throws Exception {
        switch (response.getResponseCode()) {
            case RESPONSE_NOT_FOUND:
                throw new RequestNotFound("File not found at VirusTotal dataset");
            case RESPONSE_OK:
                break;
            case RESPONSE_IN_QUEUE:
                throw new RequestInQueue("Try it again later, the request is being processed");
        }
    }

}

/**
 * Exception for api responses
 */
class RequestInQueue extends Exception {
    public RequestInQueue() {
        super();
    }

    public RequestInQueue(String message) {
        super(message);
    }
}

class RequestNotFound extends Exception {
    public RequestNotFound() {
        super();
    }

    public RequestNotFound(String message) {
        super(message);
    }
}

/**
 * Support class related to Http requests
 */
class NetworkUtils {
    public static String makeHttpRequest(String uri, Map<String, String> headers, String method,
            BodyPublisher bodyPublisher)
            throws IOException, InterruptedException {
        java.net.http.HttpRequest.Builder requestBuilder = HttpRequest.newBuilder().uri(URI.create(uri));
        if (headers instanceof Map) {
            Iterator<String> iteratorHeaders = headers.keySet().iterator();
            while (iteratorHeaders.hasNext()) {
                String key = iteratorHeaders.next();
                requestBuilder.header(key, headers.get(key));
                // System.out.println("key " + key + " value " + headers.get(key));
            }
        }

        HttpRequest request = requestBuilder.method(method, bodyPublisher)
                .build();
        HttpClient httpClient = HttpClient.newHttpClient();
        HttpResponse<String> response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());
        return response.body();
    }

    public static String buildNetworkFile(File file) throws IOException {
        byte[] sampleBytes = Files.readAllBytes(file.toPath());
        String fileBase64 = Base64.getEncoder().encodeToString(sampleBytes);
        String mimeType = Files.probeContentType(file.toPath());
        String result = "data:" + mimeType + ";name=" + file.getName() + ";base64," + fileBase64;
        return result;
    }
}

class FileUtils {
    public static File launchFileChooser() throws Exception {
        JFileChooser fileChooser = new JFileChooser();
        fileChooser.setDialogTitle("Reto #10 - MoureDev - Choose the file to scan by VirusTotal");
        fileChooser.setCurrentDirectory(new File(System.getProperty("user.home") + "\\Downloads"));

        int dialogResult = fileChooser.showOpenDialog(null);
        if (dialogResult == JFileChooser.APPROVE_OPTION) {
            return fileChooser.getSelectedFile();

        } else {
            throw new IllegalStateException("Error: No file was selected");
        }
    }
}

class Utils {
    public static void wait(int seconds) throws InterruptedException {
        String message = "Waiting until next request ";
        System.out.print(message);
        for (int i = 1; i <= seconds; i++) {
            System.out.print(i + " ");
            Thread.sleep(i * 1000);
        }
        System.out.println();
    }
}

public class codigocaballer {
    public static void main(String[] args) {
        try {
            final ScanResponse scanResponse = VirusTotalApiOperation.launchFileScan();
            Utils.wait(30);
            VirusTotalApiOperation.launchFileReport(scanResponse.getResource());

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}