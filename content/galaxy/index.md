---
title: Getting started
---

# Getting started with Galaxy Europe

[Galaxy](https://usegalaxy.eu) is a web platform for analysing biological data. You run analysis tools from your browser, and the computations run on the Galaxy Europe servers.

## Create an account

1. Go to <https://usegalaxy.eu/login/start> and register with your university e-mail address.
2. Confirm your e-mail address and log in.

## The Galaxy interface

- **Left:** the activity bar, with **Upload**, **Tools**, **Workflows** and more. Search for a tool by name in the tool panel.
- **Centre:** the tool form or the result you are viewing.
- **Right:** your current **history**, which is the list of all datasets you have uploaded or created.

Every dataset in the history has a colour showing its state: **grey** means waiting, **orange** means running, **green** means finished, and **red** means failed. Click a dataset's name to expand it. Click the **eye** icon to view its contents.

## Histories

A history holds one analysis. Start a new history for each exercise (the **+** icon at the top of the history panel), and give it a clear name.

For an exercise you will usually **import a shared history** that already contains the input data:

1. Log in first.
2. Open the link given on the [Data](../data/index.md) page.
3. Click **Import this history**. In the **Copying History** dialog, give the copy a name and click **Copy History**.
4. A blue message confirms *"History imported and is now your active history"*, but the page still shows the shared history. Click the **Galaxy** logo at the top left (*Home*) to return to the main page: your copy is now shown in the history panel on the right.

The copy is yours, and you can run tools in it. You cannot run tools in the shared history itself.

## Datatypes and collections

Galaxy uses the **datatype** of a dataset to decide which tools can read it. Compressed FASTQ files with standard quality scores have the datatype `fastqsanger.gz`. If a tool does not offer your dataset as input, check the datatype. You can change it with the **pencil** icon, under **Datatypes**.

Paired-end reads come as two files (forward and reverse). Galaxy keeps them together as a **paired collection**, so that tools always receive both files in the right order.

## Running a tool

1. Search for the tool, open it, and fill in the form as described in the exercise.
2. Click **Run Tool**. The new outputs appear at the top of your history.
3. When the outputs are green, click the eye icon to inspect them.

Tool links in the exercises open the exact tool version used in the course.

## If a job fails (red dataset)

Click the red dataset to expand it and read the error message.

- If the message mentions the **server** (for example *container creation failed*), it is a temporary problem on Galaxy Europe. Click the **Run Job Again** button (circular arrow) in the expanded dataset, and then **Run Tool** without changing anything.
- If the message is about your **input or settings**, check the tool form against the exercise instructions, correct it, and run the tool again.
- If it still fails, ask a teacher (see below).

## Getting help from a teacher

If something does not work, you can let a teacher look at your history:
open **History options** (the menu at the top of the history panel), choose **Share & Manage Access**, and share the history with your teacher's Galaxy e-mail address. Your teacher can then view the history (and copy it), but cannot change it.

## Storage

Your Galaxy account has a storage quota. Delete histories you no longer need, and choose to delete them **permanently** to free space.

## Learn more

- [A short introduction to Galaxy](https://training.galaxyproject.org/training-material/topics/introduction/tutorials/galaxy-intro-short/tutorial.html) (Galaxy Training Network)
- [Galaxy Training Network](https://training.galaxyproject.org/): many more tutorials
- [Galaxy Help forum](https://help.galaxyproject.org/)
