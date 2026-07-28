# MSU - CMSE 801 - Spring 2026

This is the CMSE 801 Spring 2026 course content repository for instructors.  Content on the `main` branch is rendered and distributed to a JupyterBook hosted here: [https://msu-cmse-courses.github.io/cmse801-S26](https://msu-cmse-courses.github.io/cmse801-S26).

## Getting started

Clone this git repository to your computer:\
`git clone https://github.com/msu-cmse-courses/CMSE801-S26.git`\
this will create a directory called `CMSE801-S26` with all the source files.

If you want to be able to build and publish the html yourself then you may find it useful to create a conda environment:\
`conda create -n cmse801`\
`conda activate cmse801`

and then installing these packages:\
`conda install -c conda-forge jupyter-book` (or `pip install jupyter-book`) \
`conda install -c conda-forge ghp-import` (or `pip install ghp-import` )

> [!WARNING]  
> Mengsen: the jupyter book only works as described below when using v<2.0.0. The following installation worked for me. \
> ```conda install conda-forge::jupyter-book==1.0.4.post1```

`jupyter-book` commands begin with `jb` and are used to build the static html (in the `_build` folder). \
The `ghp-import` package commits the content of the `_build` folder to a special branch of the repo (`gh_pages`) that hosts the JupyterBook on the github.io site.

## To create STUDENT versions of notebooks

`python makeStudentVersion.py name_of_notebook-INSTRUCTOR.ipynb`

This will create a corresponding `name_of_notebook-STUDENT.ipynb` file where
every cell that has "ANSWER" in the *first* line will be removed. This includes
both code cells *and* markdown cells.

## Adding a lesson to the main branch

To add a lesson, do the following on your terminal:

1) Make sure you are in the main branch:\
   `git checkout main`
2) Make sure the branch is updated:\
   `git pull origin main`
3) Copy the final versions of all of the files you need into that Day's folder (e.g. Day-02)
4) Create the STUDENT version of the notebook.
5) Update the `_toc.yml` file to uncomment out that day's notebooks and update the filenames if they have changed.
6) Add the notebooks and all of their dependent files and commit locally (don't forget `_toc.yml`!):\
   `git add Day-02/Day-02_Fidget_Spinners_STUDENT.ipynb Day-02/Day-02_Fidget_Spinners_INSTRUCTOR.ipynb Day-02/fidget_spinner.jpg _toc.yml`
7) Commit your work locally:\
   `git commit -m 'day 2 content'`
8) Push to the remote repository:\
   `git push origin main`
9) Publish to the github.io site:\
   `jb build .`\
   `ghp-import -n -p -f _build/html`
   
   or alternatively for Mac:\
   `./build_and_deploy.sh`\
   for Windows:\
   `./build_and_deploy.bat`

## Generate and presenting slides using jupyter notebook

### install RISE for creating slides and presenting
It's easier to use [RISE](https://rise.readthedocs.io/en/latest/) to do it. 

You need to check your jupyter notebook version because 6 and 7 works very differently:

```jupyter notebook --version```

It works the best with Notebook 6 or lower (classical jupyter notebook). To install:

```conda install -c conda-forge rise```

or 

```pip install RISE```

For notebook 7 +,

```conda install conda-forge::jupyterlab_rise```

or

```pip install jupyterlab_rise```

### use RISE for creating slides

For Notebook 6- (classical notebook), you can follow [this](https://mljar.com/blog/jupyter-notebook-presentation/) tutorial. In short, you just need to click `View` &rarr; `Cell Toolbar` &rarr; `Slidesshow`. Then there should be a dropdown in each cell to select the slide type. 

For Notebook 7+, you will need to click `View` &rarr; `Right SideBar` &rarr; `Show Notebook Tools`. Then a toolbar should show up on the right. For each cell, you can set the property `Slide Type` under `COMMON TOOLS`.

### use RISE for presenting slides
For Notebook 6- (classical notebook), there should a button under the menu to start the slide show at any cell. 

For Notebook 7+, there should be an option `View` &rarr; `Render as Reveal Slideshow`. You may also have a little button under the menu to the right. 

If something doesn't work, just double check `jupyter --version` and make everything is installed (`notebook`,`nbconvert`,etc.) in compatible version.

### export slides as pdf
You can follow the [doc](https://rise.readthedocs.io/en/latest/exportpdf.html).

1. Generate html slides and show it\
```jupyter nbconvert --to slides your_talk.ipynb --post serve```

2. Right click &rarr; print &rarr; save as pdf. Use landscape would look better. 