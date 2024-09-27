
class Main {
  public static void main(String[] args) {
    String url = "https://retosdeprogramacion.com?year=2023&challenge=0";
    getParams(url);

  }

  public static void getParams(String url) {
    String paramsUrl = url.split("\\?")[1];
    String[] keyValueParams = paramsUrl.split("&");
    int paramsSize = keyValueParams.length;
    String[] params = new String[paramsSize];
    System.out.print("[");

    for (int i = 0; i < paramsSize; i++) {
      String param = keyValueParams[i];
      String value = param.split("=")[1];

      params[i] = value;

      if (i == paramsSize-1)
        System.out.print(", ");

      System.out.print(value);

    }
    System.out.print("]");

  }

}
