import PyWay2SMS



def test_split_message():
    max_chars = 156
    ellipsis = " .."
    message = "apple"*(400//5)
    expected_output = [
        "apple"*30 + "app" + " ..",
        " .." + "le"+ "apple"*29 +"app"+ " ..",
        " .." + "le"+ "apple"*19
    ]
    result = PyWay2SMS.split_message(message,max_chars,ellipsis)
    for i in range(0,len(result)):
        print(result[i])
        print(expected_output[i])
        print()
        assert expected_output[i] == result[i]

