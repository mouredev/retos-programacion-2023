const url = "https://retosdeprogramacion.com";

function getParamsValues(url) {
    const urlParams = url.slice(url.indexOf("?") + 1).split("&");
    if (
        urlParams[0] == url ||
        urlParams[0] == "" ||
        urlParams[0].endsWith("=")
    ) {
        return [];
    } else {
        return urlParams.map((param) => param.slice(param.indexOf("=") + 1));
    }
}
