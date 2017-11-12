#Victoria Slater and Jason Karos
#COM 214 HW 1
#Due Wednesday 2/8/17 end of day
#Victoria Work Division Assessment: Jason - 50%, Victoria - 50%
#Jason Work Division Assessment: Jason - 50%, Victoria - 50%



from random import*
from time import *

def wrap(tag, string):

    #user gives you <html> and "string" (parameters)
    #and you have to put </html> at end

    startTag = "<" + tag + ">"
    
    endTagSplit = tag.split()
    endTag = "</" + endTagSplit[0] + ">"
    #if userInput == ("<html>", "string"):
    #print(startTag, string, endTag)
    return(startTag + string + endTag)


#wrap("html", "string")
#def makeTableString(content, dimensions):

    #user provides dimensions and content as a list,
    #an HTML table of said dimensions is constructed and filled
    #with content from the list in the order it is provided.


#makeTableString(content, dimensions)

def getTableDim(tableRows):

    #given a list of table rows, returns proper dimensions to suit said table.
    y = len(tableRows)
    tempRow = tableRows[0].split()
    x = length(tempRow)
    return x,y

#getTableDim

def genImageTable(imageRows):
    tableString = ""
    for y in imageRows:
        row = y.split()
        rowString = ""
        for x in row:
            td = wrap("td","<img src=\"images\\"+x+"\" width=\"100\" height=\"100\"/>")
            rowString = rowString+td
        tableString = tableString + wrap("tr",rowString)
    tableString = wrap("table",tableString)
    return tableString

#genImageTable

def genLetterTable(letters, dimensions, cellColor1, cellColor2):
    yDim = eval(dimensions[0])
    xDim = eval(dimensions[1])
    temp = 51
    tableString = ""
    cellColors = [cellColor1, cellColor2]
    q = 0
    for y in range(0,yDim):
        rowString = ""
        for x in range(0,xDim):
            td = wrap("td style=\"background-color:"+cellColors[q%2]+"\"",letters.pop(randrange(0,temp)))
            rowString = rowString + td
            temp = temp - 1
            q = q + 1
        tableString = tableString + wrap("tr",rowString)
    tableString = wrap("table",tableString)
    return tableString

#genLetterTable

def genHTML(config):
    configRead = config.readlines()

    #color and stuff for html code
    bodyBackground = configRead[0]
    bodyBsplit = bodyBackground.split()
    #print(bodyBsplit[1])
    #backString = "body {background-color:",bodyBsplit[0],";}"
    #wrap("style",backString)
    #print(backString)
    
    cellBackground1 = configRead[1]
    cellB1split = cellBackground1.split()
    #print(cellB1split[1])
    
    cellBackground2 = configRead[2]
    cellB2split = cellBackground2.split()
    #print(cellB2split[1])
    
    tableBorderColor = configRead[3]
    tableBCsplit = tableBorderColor.split()
    #print(tableBCsplit[1])
    
    tableBorderPx = configRead[4]
    tableBPxsplit = tableBorderPx.split()
    #print(tableBPxsplit[1])
    
    authors = configRead[5]
    authorsSplit = authors.split()
    #print("Authors: ", authorsSplit[1:4])

    title = configRead[6]
    titleSplit = title.split()
    #print(titleSplit[1])

    mode = configRead[7]
    modeSplit = mode.split()

    #print("configRead 7:",configRead[7])
    if modeSplit[0] == "IMAGES": 
        imageRows = configRead[8:]
        tableString = genImageTable(imageRows)
        #print("IMAGETABLE:",tableString) 

    ##    imagesRow2 = configRead[9]
    ##    imagesRow2split = imagesRow2.split()
    ##    print(imagesRow2split)
    ##
    ##    imagesRow3 = configRead[10]
    ##    imagesRow3split = imagesRow3.split()
    ##    print(imagesRow3split)


        #generate letters
        #uppercaseletters = ASCII 65 - 91
        #lowercaseletters = ASCII 97 - 124

    #elif configRead[7] == "LETTERS":

    else:
            
        tableDimensions = configRead[8].split("x")
        tableLength = tableDimensions[0]
        #print("The table is ", tableLength, "cells long")
        tableWidth = tableDimensions[1]
        #print("The table is ", tableWidth, "cells wide")
        alphabet = []
        for i in range(65, 91):
            upperLetter = chr(i)
            alphabet.append(upperLetter)
#           print(chr(upperLetter))
        for i in range(97, 124):
            lowerLetter = chr(i)
            alphabet.append(lowerLetter)
#            print(chr(lowerLetter))
        tableString = genLetterTable(alphabet, tableDimensions, cellB2split[1],cellB1split[1])
        #print("LETTERTABLE:",tableString)
    bodyString = tableString
    titleString = wrap("h1",titleSplit[1])
    authorString = ""
    for x in range(1, len(authorsSplit)):
        authorString = authorString+authorsSplit[x]+" "
    #print(authorString)
    authorString = "Authors: "+authorString
    authorString = wrap("p",authorString)

    dateString = strftime("%Y-%m-%d %H:%M:%S")
    dateString = wrap("p", "Current Date and Time: "+dateString)

    bodyString = titleString + bodyString + dateString +authorString
    bodyHTML = wrap("body",bodyString) 

    headTitleString = wrap("title",titleSplit[1])

    bodyStyleString = "body {background-color:" + bodyBsplit[1] + ";}"
    tableStyleString = "table {border:" + tableBPxsplit[1]+ "px solid " + tableBCsplit[1]+";border-collapse:collapse;margin:auto;text-align:center;width:60%;}"
    pStyleString = "p {text-align: center;}"
    tdStyleString = "td {border: 1px solid darkblue;}"
    h1StyleString = "h1 {text-align: center;}"
    styleString = bodyStyleString + tableStyleString + tdStyleString +pStyleString + h1StyleString
    styleString = wrap("style type=\"text/css\"", styleString)
    #print(styleString)

    headerString = headTitleString + styleString
    headerHTML = wrap("head", headerString)
    #print(headerHTML)
    print(bodyHTML)
    htmlHTML = headerHTML + bodyHTML
    htmlHTML = wrap("html", htmlHTML)
    htmlHTML = "<!DOCTYPE html>" + htmlHTML 
    return htmlHTML
#genHTML

def main(): 
    inFile = open("config.txt", "r")
    html = genHTML(inFile)
    outFile = open("hw1.html", "w")
    outFile.write(html)

    

main()







    
