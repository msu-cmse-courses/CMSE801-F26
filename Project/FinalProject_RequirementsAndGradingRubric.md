# CMSE 801 Final Project - Requirements and Grading Rubric

## Overall requirements

For your semester project, you'll be expected to turn in

- **A Jupyter notebook,**
- **Slides used in the presentation**.

### Jupyter Notebook

Your **Jupyter notebook** should contain the following:

- All the code used to complete your project. The code should be documented so that the instructor can understand what you did and why you did it. This means including meaningful comments in the code itself! You should also use logical variable names to ease the reading of the code.
- Narrative text (using Markdown cells) that explains what you did, why you did it, and how you went about it. You should break the notebook up into the following meaningful sections so that the instructor can follow the logical flow of your work:

  - **Background and Motivation**: Provide some context for the problem and what question(s) you set out to answer.
  - **Methodology**: How did you go about answering your question(s)? Most of your code will be contained in this section.
  - **Results**: What did you find when you carried out your methods? Some of your code related to presenting results/figures/data may be replicated from the methods section or may only be present in this section.  All of the plots that you plan on using for your presentation should be present in this section.
  - **Synthesis and Discussion**: What did you learn from your results? What obstacles did you run into? What would you do differently next time? What is the answer to your question(s) and why?

**The code, text, and visuals should be threaded together as coherent report of your work!**

### Presentation

In addition to the notebook, **you will be giving a _no more than 4 minute_ presentation in class** using a short set of slides to share the results of your project with your fellow classmates and your instructors. Your presentation should include appropriate **visual aids**. The presentation should address:

- The **question(s)** you set out to answer.
- The **model** that you applied to your chosen data or chosen topic.
- The **computational techniques** that you used to analyze your data or run your model.
- The **answer(s)** you arrived at.


#### Details on presentation slides

You can create your slides using the presentation software of your choosing (e.g. Google Slides, Powerpoint, Keynote). Once you've finished your slides, you should save a **PDF copy** that you can submit with your Jupyter notebook. You should aim for having a reasonable number of slides -- a good guideline is ~1 min of time per slide. For a presentation of this length, you probably wouldn't want to have more than 6 slides, realistically, but you should make sure that you have a sufficient number of slides to support your presentation.

**The slides should**:

- Address the above points in a logical order.
- Include a title slide with your project title, name, and course number (with section number).
- Effectively communicate information through a combination of text and figures. Text and figures should be clearly legible in your presentation.
- Only include text and figures that support the presentation (avoid including content "just because").
- Avoid large paragraphs of text, use bullet points instead.

If you would like to try to make presentation slides using a Jupyter Notebook visit this [site](https://rise.readthedocs.io/en/latest/). Note that this is **not** a requirement, but a nice tool that has been used for the beginning of class presentations given by the instructor. Note that the newest version of Jupyer Notebook makes using RISE a little harder to use and the installation process, contact your instructor if you would like help getting this setup on your computer.

<!-- ### Additional details on Live Presentations and/or Recorded Presentations

In addition to creating your presentation slides, you are expected to make a recording of your presentation. You should use Zoom to record your presentation. You should be able to "Share Screen" in Zoom to share your slides and talk through the presentation as if you were giving it live. **You should make sure that your recording is no longer than 5 minutes, but it should be at least 4 minutes.** You will turn in the "mp4" file that Zoom produces when your record the Zoom session. -->

## Grading Rubric

The presentation/project will be graded as follows (**total: 100 points**):

- Oral presentation (**20 points**). Is it clear and well-structured? Does the student effectively communicate the key ideas about their results?
  - *Excellent presentation*: student speaks clearly and in a logical manner, and makes their key points clear. (**20 points**)
  - *Good presentation*: student speaks clearly and logically and conveys key points, but presentation is somewhat lacking (**15 points**)
  - *Fair presentation*: student's oral presentation is substantially lacking (speaking too quietly to be heard or with little inflection, clarity/logical flow in speaking is sub-par, etc.) (**10 points**)
  - *Poor presentation*: student's oral presentation is completely lacking (cannot be heard, there is no logical progression to the presentation) (**5 points**)

- Presentation slides (**20 points**). Do the slides complement the oral presentation, and conform to the guidelines?
  - *Excellent slides*: Slides conform to specifications in final presentation document, including number of slides, adequately addressing all points, legibility. Slides complement oral presentation. (**20 points**)
  - *Good slides*: Slides deviate from specifications in some minor way: too many or too few slides, not all points addressed, some slides hard to understand (poor graphics, too much or too little text, etc.) (**15 points**)
  - *Fair slides*: Slides deviate from specifications in some substantial way: too many or too few slides, half or fewer of points addressed, most slides hard to understand (poor graphics, too much or too little text, etc.) (**10 points**)
  - *Poor slides*: Slides do not conform to specifications in any meaningful way. (**5 points**)

- Final project content (**40 points**). This is a combination of the content in the student's presentation and in their Jupyter notebook. Does the student clearly and concisely address all off the points listed in the final project guidelines?
  - *Excellent content*: All points clearly and concisely addressed. (**40 points**)
  - *Good content*: Most of the points clearly and concisely addressed, or all points nominally addressed but some are unclear. (**30 points**)
  - *Fair content*: Roughly half of the points clearly and concisely addressed, or all points nominally addressed but half are unclear.(**20 points**)
  - *Poor content*: Few of the points clearly and concisely addressed, or most/all points nominally answered but most are unclear. (**10 points**)

- Coding practices (**10 points**). What is the quality of the code that is written? Does the code have adequate comments? Do the variable names make sense? Your instructor should be able to read through your code and understand what it is doing and why. Is the data managed effectively and efficiency such that it is easy to understand how the data is being manipulated? Are variables clearly identified? Are appropriate data types used (dataframes vs. numpy arrays etc.)? Look at the code in pre-class and in-class assignments to get a sense for the level of detail you should include. Your instructor **likely will not run your notebook** on their computer, but they should be able to if they want. Therefore, `Restart and Run All` cells before submitting your notebook and make sure there are no errors and warnings. In addition, your final notebook should have a section at the very beginning explaining how to run the notebook and any additional files needed for it. Alternatively, you can write a `README.md` file and upload it on D2L with your notebook.
  - *Excellent content*: There are clear instructions on how to run the notebook and its additional files. The notebook runs without errors and/or warnings. The code is well documented and easy to understand. The notebook is divided into sections and subsections. Each code cell has comments and it is accompanied by a markdown cell explaining what the code cell is doing. (**10 points**)
  - *Good content*: There are no clear instructions on how to run the notebook, files are missing, but the notebook is without errors and/or warnings. The code is documented, but the notebook lacks organization in sections and subsections. Code cells have few comments and no markdown cells explanation. (**6 points**)
  - *Fair content*: The notebook runs but it is not well documented. It is difficult to understand what code cells are doing. Template text has been left in the notebook (**2 points**)
  - *Poor content*: The notebook does not run and there are no support structures (e.g. comments) to help the reader understand the code.  (**0 points**)

- Peer assessment (**10 points**). During the presentations, you will be required to evaluate your peers' presentation using a provided rubric. Being present for the project days and completing these peer evaluations will make up this portion of your grade.
