Cuerdo, Marjorie Ann  
Fielder, Sabrina  
Lietz, Rebecca  

# Wave Function Collapse for Poetry

This is adapted code from https://github.com/mewo2/oisin for performing the WaveFunctionCollapse algorithm to create poems. 
It mashes up sentence fragments from a given text file to produce poems with fixed metric forms. 

# Example output
<img src="https://raw.githubusercontent.com/marjcuerdo/wfc_poetry/main/output/bible.png" width="355" height="305">

[Harry Potter Example - Full Output Text File](https://raw.githubusercontent.com/marjcuerdo/wfc_poetry/main/output/output_harrypotter1_1.txt)  
[Holy Bible Example - Full Output Text File](https://raw.githubusercontent.com/marjcuerdo/wfc_poetry/main/output/output_bible_1.txt)

It can also animate the process:  
![GIF of Holy Bible Output](https://raw.githubusercontent.com/marjcuerdo/wfc_poetry/main/output/bible.gif)

# Instructions 

* Clone this repository 

or 

* Download the zipped folder and unzip it to your desired location.

## If you do not have pip installed

* Open your command prompt/terminal.

* Navigate to the folder that has Python.

* Copy and paste the following commands and run them one at a time:

  `curl https://bootstrap.pypa.io/ez_setup.py -o - | sudo python`

  `sudo python get-pip.py`

* Install required packages to run the algorithm

  `pip install -r requirements.txt`

## Generate poetry text file

* Navigate `cd` to where you unzipped the `wfc_poetry` folder.
* Enter the following code (defaults to `ballad` format):

  `python ballad.py [input/yourTextFileName.txt]`

## Generate animated GIF

* Enter the following code:

  `python makegif.py [input/yourTextFileName.txt] [numberOfLinesToAnalyze] [output/yourGifFileName.gif]`

# More information

## Modifying text output
We updated `ballad.py` to receive the chosen poetry type from the user, if they want a format other than the default `ballad`.

  `sonnet = iambic(5, 'ababcdcdefefgg')`  
  `petrarch = iambic(5, 'abbaabbacdecde')`  
  `ottava = iambic(5, 'abababcc')`  
  `couplet = iambic(5, 'aa')`  
  `ballad = iambic(4, 'a') + iambic(3, 'b') + iambic(4, 'a') + iambic(3, 'b')`   
  `verse = iambic(5, 'abcb')`  
  `blank = iambic(5, 'abcd')` 

For example, specifying the `couplet` poetry type would look like below (using the `harrypotter1.txt` file):
  
  `python ballad.py input/harrypotter1.txt couplet`
  
[Harry Potter Couplet Example - Full Output Text File](https://github.com/marjcuerdo/wfc_poetry/blob/main/output/output_hp1_couplet.txt)  

## Modifying GIF output

Similarly, this can be done for `makegif.py` by entering:

  `python makegif.py input/harrypotter1.txt 300 output/hp1_couplet.gif couplet`
  
This results in:

![GIF of HP Couplet](https://github.com/marjcuerdo/wfc_poetry/blob/main/output/hp1_couplet.gif)


