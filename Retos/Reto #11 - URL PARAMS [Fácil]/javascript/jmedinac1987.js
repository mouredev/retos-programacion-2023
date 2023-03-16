function getParamsValues(url) {
  if (url === undefined) return ["Error: undefined"];

  try {
    let params = [];
    let arrayText = [];
    let arrayAux = [];

    if (!url.includes("?")) return ["Error: no arguments"];
    if (!url.includes("=")) return ["Error: arguments without values"];

    arrayText = url.split("?");

    if (arrayText[1].includes("&")) {
      arrayAux = arrayText[1].split("&");

      arrayAux.forEach((value) => {
        params.push(value.split("=")[1]);
      });

      return params;
    }

    arrayAux = arrayText[1].split("=");

    if (arrayAux.length > 2) {
      return ['Error: multiple arguments without "&" separator'];
    }
    params.push(arrayAux[1]);

    return params;
  } catch (error) {
    return [`Error: ${error}`];
  }
}

//Tests
let testUrlOne = "https://test/_testPlans/define?planId=00001";
let testUrlTwo =
  "https://test/test/acc/home/cxapp/support/agent/pay/system/tickets/list/all-cases?frameorigin=https%3A%2F%2Fone.testing.com&user=qa";
let testUrlThree =
  "https://newinformation/_layouts/15/Doc.aspx?sourcedoc={befa3d19-a05d-4e1f-b2f9-cfcc013f8443}&action=edit&wd=target%28Test%20Data%20-%20Merchant%20Accounts.one%7C25d757ff-c6ff-4611-b28e-c80af9562c50%2FTest%20Data%20%E2%80%93%20Merchant%20Accounts%7C987d152e-6be3-406c-8a4d-8227369b6fba%2F%29&wdorigin=NavigationUrl";
let testUrlFour = "https://test/_testPlans/define";
let testUrlFive = "https://test/_testPlans/define?planId00001";
let testUrlSix = "https://test/_testPlans/define?planId=00001planId2=00002";

console.log(getParamsValues(testUrlOne));
console.log(getParamsValues(testUrlTwo));
console.log(getParamsValues(testUrlThree));
console.log(getParamsValues(testUrlFour));
console.log(getParamsValues(testUrlFive));
console.log(getParamsValues(testUrlSix));
console.log(getParamsValues());
