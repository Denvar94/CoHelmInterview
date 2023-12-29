# CoHelmInterview
Repo for the CoHelm records task

## How to run
First build the docker image
`docker build -t [IMAGE_NAME]`

Next make sure that the `$OPENAI_API_KEY` has the access token needed to use the Open AI key.
Now place any medical records in the data folder, `src/data/medical_records.pdf`

To run the AI Pipeline, enter the following Docker command

`docker run -e OPENAI_API_KEY=$OPENAI_API_KEY --name [NAME_OF_CONTAINER] [IMAGE_NAME] -m src/data/[medical-record-filename]`

We can also use another guideline, but it has to be in a text file. Use the following command to run your own guideline

`docker run -e OPENAI_API_KEY=$OPENAI_API_KEY --name [NAME_OF_CONTAINER] [IMAGE_NAME] -m src/data/[medical-record-filename] -g [src/data/guidline_filename]`

## How does it work
The pipeline uses the OpenAI chat-gpt-4 model to answer the questions given in the task.

### Reformat medical record
The first step is to run the medical records through a pdf reader in python, this output a long string with all the text from the pdf.
Since this pdf isn't formatted, I ask the chat bot to format the medical records and divide into paragraphs we appropiate headings.
At this point I also tell the chat bot that the string has artifacts and to fill out any words that seem to have missing letters. I also 
tell the LLM to include dates and try to infer dates from the text and have them explcity mentioned.

### Get CPT code
Here I ask the chatbot to give the requested CPT code for the procedure, ignoring any CPT codes that were past procedures.
It is important to note that given a database of CPT codes we could easily check each token and return only the CPT codes in our database.
We could then make sure the context of the cpt code was the one requested. This would avoid using an LLM.

### Check for previous conservative treatment
This section was tricky. Here I asked the chat bot whether there was any conservative treatments that improved the condition. I ask this question 
on every paragraph, the LLM seemed to find it tricky to find previous treatment in medical record 1 under notes. I believe that it gets confused
when it sees previous medical histories under different headings. As a result by sending each paragraph, I check in each paragraph for previous treatments.
Now when the LLM sees just the notes, it is able to answer correctly that the treatment had been recieved and was succesful.

### Guidlines
The trickies part was to convert the guidlines into insutructions for the LLM. Since the task was so that this approach could be generalized,
it made it incredibly tricky.

Here I ask the LLm to take the guidlines and create a step by step instruction set to perform on the medical records. I tell it that criteria doesn't
need to all the steps to be fulfilled to be met and also once we have met the criteria for a procedure, stop the steps.
Once I had generated the steps, I ask the LLM to apply the steps to the medical given.

This approach seemed to work on the medical records given however it is not robsut. Repeated runs on this pipelien produces different steps each time.
Given that we wouldn't know what guidelines we expect to see, the task at hand is increidbly difficult. 

Using the steps approach, we could develop this further to make the LLM steps more robust. Possibly by using the indents given by the guidelines to 
generate the steps line by line rather than one go and feeding the LLM with more prompts might generate better steps.

Generally, once the steps had been defined the LLM was pretty accurate in answering the questions in the steps.

I hope this approach is impressive enough and was a fun task!

