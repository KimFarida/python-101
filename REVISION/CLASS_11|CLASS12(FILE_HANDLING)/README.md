Basic File Operations
    File Concepts and Modes 
    Reading Files 
    Writing Files
    Context Managers 


CSV File Handling
    CSV Module Introduction 
    Reading CSV Files
    Writing CSV Files 
    Advanced CSV Operations 


QUESTIONS
"What might go wrong if we don't close a file properly?"
"Why would we choose 'w' mode over 'a' mode?"
"When would you use readline() vs readlines()?"
"What are the advantages of using the csv module over manual string splitting?"
"How would you handle a CSV file with missing values?"

Common Pitfalls to Highlight

Not closing files properly
Forgetting to handle encoding issues
Using write mode when append is needed
Not handling file not found exceptions
Assuming CSV structure without checking headers

Additional Tips

Always use context managers (with statement)
Handle encodings explicitly
Consider memory usage with large files
Validate file existence before operations
Keep backup copies when writing files

ASSIGNMENT CRITERIA
Proper file handling (opening/closing)
Error handling implementation
Code organization and documentation
Efficient file reading/writing
CSV data processing accuracy
Input validation
Resource management

RECOMMENDED READING
File Handling Resources:

File Objects: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
Built-in Functions: https://docs.python.org/3/library/functions.html#open
io Module: https://docs.python.org/3/library/io.html
os.path Module: https://docs.python.org/3/library/os.path.html

CSV Operations:

csv Module: https://docs.python.org/3/library/csv.html
Reading/Writing CSV: https://realpython.com/python-csv/
pandas CSV Operations: https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html

Practice Resources:

Python Exercises: https://www.w3resource.com/python-exercises/file/
CSV Processing Examples: https://realpython.com/python-csv/
File Handling Problems: https://www.geeksforgeeks.org/file-handling-python-set-1/

Slides
https://docs.google.com/presentation/d/1G1p9nslbWx9F4VfY_e9ovmFQxrC1iyl4ucOaRJHAvaI/edit#slide=id.g30a1792efa8_0_103
https://docs.google.com/presentation/d/1FtDJ9-9gE2R-Z9EgXTY9QVeUWWnjdVUvupAKOHfRlqM/edit#slide=id.g30a9abd6eca_0_82
