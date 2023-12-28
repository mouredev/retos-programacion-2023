program Mariopolonia0;

uses SysUtils, DateUtils;

var
  month, year: Word;
  date: TDateTime;

begin
  Write('Enter the number of the month:');
  ReadLn(month);

  Write('Enter year:');
  ReadLn(year);

  // agrego la fecha
  date := EncodeDate(year, month, 13);

  if DayOfWeek(date) = 6 then
    WriteLn('The 13th is Friday')
  else
    WriteLn('The 13th is not Friday');
    
end.
