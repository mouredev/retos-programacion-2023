function isThereFridayThe13th(year, month) {
    try {

      let numberDaysOfTheMonth = new Date(year, month, 0).getDate();
      let isThereFridayThe13 = false;
      let weekdays = ["Sunday","Monday","Tuesday","Wednesday",
                      "Thursday","Friday","Saturday",];
  
      for (let day = 1; day <= numberDaysOfTheMonth; day++) {
        
        let index = new Date(year, month - 1, day).getDay();
        let numberAndDay = `${day}-${weekdays[index]}`;
  
        if (numberAndDay.includes("13-Friday")) {
          isThereFridayThe13 = true;
          break;
        }
      }
  
      return isThereFridayThe13;
    } catch (error) {
      return false;
    }
  }

  //Test cases
  console.log(isThereFridayThe13th(2023,1));
  console.log(isThereFridayThe13th(2023,2));
  console.log(isThereFridayThe13th(2023,10));