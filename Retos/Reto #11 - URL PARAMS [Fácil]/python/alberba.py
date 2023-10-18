def extract_values(url: str) -> list:
    parameters = url.split("?")[1]
    values = parameters.split("&")
    value_list = []
    for value in values:
        value_list.append(value.split("=")[1])
    return value_list

print(extract_values("https://www.youtube.com/watch?v=EKj8qJrC0T8&ab_channel=ToroTochoReviews"))
