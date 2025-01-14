class Test:
    def __init__(self: "Test", test_attr: "str", test: "str")-> "Test":

        assert(type(test) == str)
        self.test_attr = test_attr
        (body, method_signature, attributes) = create_test(self.test_attr, test)
        
        self.body = body
        self.method_signature = method_signature
        self.attributes = attributes

    def __str__(self):
        to_ret = ""
        for line in self.attributes:
            to_ret += line + "\n"
        to_ret += self.method_signature + "\n"
        for line in self.body:
            to_ret += line + "\n"
        return to_ret

totalTestIndex = 0

# Given a single string that represents a test, returns the different components of the test
def create_test(attr: "str", test: "str")-> "tuple":
    global totalTestIndex
    if totalTestIndex is None:
        totalTestIndex = 0
    attributes = list()
    line_idx = 0
    test_as_list = test.split("\n")
    while "public" not in test_as_list[line_idx]:
        if len(test_as_list[line_idx]) > 0:
            attributes.append(test_as_list[line_idx])
        line_idx += 1
    slice_idx = attributes[0].index('[')
    indentation = attributes[0][:slice_idx]
    # attributes.insert(0, indentation + attr)
    attributes.insert(0, indentation + attr)
    splitLine = test_as_list[line_idx].split("PUT")
    assert(len(splitLine) == 2)
    splitLine[1] = str(totalTestIndex)+ splitLine[1]
    totalTestIndex = totalTestIndex + 1
    method_signature = 'PUT'.join(splitLine)
    line_idx += 1
    body = list()
    while line_idx < len(test_as_list):
        body.append(test_as_list[line_idx])
        line_idx += 1
    return (body, method_signature, attributes)
    
        
    

        