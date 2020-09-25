# Reflection by Katie Burgess

## Using a fenced code block, please display an output from running your program

```

The contacts file contains 100 people in it! Let's get searching!

  We are looking for contacts who have a job related to insurance

  aaronhunter@gmail.com is a Surveyor, insurance
  davidgay@gmail.com is a Surveyor, insurance
  aduran@gmail.com is a Insurance broker
  cantujessica@gmail.com is a Insurance broker

Wow, we found some contacts! Email them to learn about your job!

```

## Explain `contacts_list = search.search_for_email_given_job("writer", contacts_database)`

This line of code runs the search_for_email_given_job function. It searches the contacts_database file for a writer job and assigns relavent jobs to contacts_list. The search function starts with 'search.' because the funciton isn't defined in the __main__.py file. It is defined in search.py, and so it has to have 'search.' in the front in order to tell the code runner to look for the search code file in order to run the function.

## Explain `if len(contacts_list) == 0`

This line of code calculates the list of 'contacts_list' and then checks if it is equal to 0 or not. If there are no values inside of contact_list (meaning that the length of the list would be equal to 0), then the code nested under the if statement will be run, but if there are any values in contact_list, then the nested code will be skipped.

## Please use one paragraph to explain the meaning of the following code segment

```
if job_description in current_contact_job.lower():
            contacts_list.append(contact_line)
```

This segment of code adds values to contact_list. If the job description (one of the values entered into the main function) matches a job description from the contacts file, then that line will be added to the contacts_list and then printed using typer later in the program.

## Please use one paragraph to explain the meaning of the following test case

```
def test_find_one_matching_result():
    """Check to ensure that search for contacts works for one match."""
    contacts_database = """kylebarnes@hotmail.com,Records manager
joe70@yahoo.com,Network engineer
torresjames@white.info,Electrical engineer
shawkins@watson.com,Science writer"""
    contacts_list = search.search_for_email_given_job("writer", contacts_database)
    assert len(contacts_list) == 1
```

This test case sets a custom contacts database, and searches the database for the writer keyword. If the program runs correctly, then the length of the contact list should be 1, and the assertion should return True. If there are bugs in your code, the output will likely be different, leading to the assertion being False, letting you know there is an issue you need to fix.

## What was the greatest technical challenge that you faced and how did you overcome it?

The greatest technical challenge I had was fixing the errors in my __main__.py file. I followed along during the live coding session on Youtube today, but something was still wrong with my code. I previously made corrections to what I had before, but with every correction I made I was still getting the same error. I was looking for the error for a while, until I realized that it wasn't anything I was doing, I was just forgetting to save before I was running my code again. I felt silly for missing this simple error, but it taught me to make sure I am paying attention and making sure everything is saved before I run my code.

## After completing this assignment, what is task that you want to practice more? Why?

I want to practice copying directories more often. I always feel like I am doing it wrong, and when it comes to the due date for the programs you won't be able to find mine, and so I will be missing a huge part of my grade. I want to make sure that I am doing everything correctly, so you can find my work and grade it when it is due.

## After completing this assignment, what is one experience for which you are grateful?

I am grateful for my experience during the live coding session today. I felt like I was able to keep up a lot easier today, and because of that I had a better understanding of the code and what it does. I'm grateful that I was able to have this experience, as it has shown me that I am slowly getting better at the skills we are practicing in class. I can't wait to work on further practicals, labs, and challenges in order to futher grow and develop my skills as a computer science student.
