# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os.path
from os import path
from random import choice, randint

wordFilename = "wordList.txt"
treeDepth = 4
treeBreadth = 8
numberOfScavengerNotes = 5
studentList = [("arana", 32586142386)]

class Node(object):
    def __init__(self, data):
        self.nodeList = []
        self.data = data

    def getNode(self, listPosition):
        return self.nodeList[listPosition]

    def getNodesList(self):
        return self.nodeList

    def getNodeData(self):
        return self.data

    def getNumberOfNodes(self):
        return len(self.nodeList)

    def printTree(self, prefix):
        print(f"{prefix}{self.data}")
        if len(self.nodeList):
            for node in self.nodeList:
                node.printTree(prefix + '\t')


def generateWordList(filename):
    wordList = []
    with open(filename, 'r') as wordFile:
        for line in wordFile.readlines():
            wordList.append(line.strip())
    return wordList


def buildTree(node, depth, breadth, words):
    for nodeCount in range(0, randint(3, breadth)):
        newWord = choice(words)
        # print(f"Depth: {depth} {newWord}")
        newNode = Node(newWord)
        node.nodeList.append(newNode)
        if depth > 0:
            buildTree(newNode, depth -1, breadth, words)
    return True


def chooseNodes(numberOfNodes, depth, breadth, directoryTree):
    nodeList = []
    for nodeNumber in range(0, numberOfNodes):
        currentPath = []
        destinationLevel = randint(2, depth)
        currentPath.append(destinationLevel)
        directoryNumber = randint(0, directoryTree.getNumberOfNodes() - 1)
        currentNode = directoryTree.getNode(directoryNumber)
        currentPath.append((0, directoryNumber, currentNode.getNodeData()))
        for currentLevel in range(1, destinationLevel):
            directoryNumber = randint(0, currentNode.getNumberOfNodes() - 1)
            nextNode = currentNode.getNode(directoryNumber)
            currentPath.append((currentLevel, directoryNumber, nextNode.getNodeData()))
            currentNode = nextNode
        nodeList.append(currentPath)
    return nodeList


def buildPathList(nodesList):
    directoryPaths = []
    for list in nodesList:
        currentPath = os.path.sep
        for directory in list[1:]:
            currentPath = path.join(currentPath, directory[2])
        directoryPaths.append(currentPath)
    return directoryPaths


def buildDirectories(rootPath, node):
    directoryName = node.getNodeData()
    try:
        os.mkdir(path.join(rootPath, directoryName))
    except FileExistsError:
        pass
    currentNodesList = node.getNodesList()
    if len(currentNodesList):
        for node in currentNodesList:
            buildDirectories(path.join(rootPath, directoryName), node)


def buildScavengerNotes(rootPath, pathList, prizevalue):
    currentPath = rootPath
    for directoryNumber, directoryPath in enumerate(pathList):
        folderList = directoryPath.split(os.path.sep)
        outputText = '\n'.join(folderList[1:])
        fullFilename = path.join(currentPath, f"clue_number_{directoryNumber}")
        with open(fullFilename, 'w') as clueFile:
            clueFile.write(outputText + '\n')
        currentPath = path.join(rootPath, directoryPath[1:])
    with open(fullFilename, 'w') as prizeFile:
        prizeFile.write(f"{prizevalue}")

    pass

if __name__ == '__main__':
    wordList = generateWordList(wordFilename)
    treeRoot = Node(choice(wordList))
    buildTree(treeRoot, treeDepth, treeBreadth, wordList)
    treeRoot.printTree('')
    chosenNodes = chooseNodes(numberOfScavengerNotes, treeDepth, treeBreadth, treeRoot)
    directoryPathList = buildPathList(chosenNodes)
    for studentName, prize in studentList:
        userHomeDir = os.path.expanduser('~' + studentName)
        buildDirectories(userHomeDir, treeRoot)
        buildScavengerNotes(path.join(userHomeDir, treeRoot.getNodeData()), directoryPathList, prize)

    pass
