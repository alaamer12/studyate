from enum import Enum
DIRS = ['resources', 'framework', 'design patterns', 'distributed systems']

MAIN_DIR = 'language'

class EXTENSIONS(Enum):
    TXT = '.txt'
    TEXT = '.text'
    ATE = '.ate'

DIR_DEFINITIONS = {
    'modules': """
< !-- >
Use this file to store your notes about programming language modules.
There are many types of modules, and they depend on what you want to learn and achieve.
In this modules.txt file, I have provided modules that will make you proficient in Python 
in general. The modules I have included cover various topics, starting from binary to AI tools. 
I have included simple AI tools so you can get a glimpse of AI, but I haven't covered 
everything you would need to become a data science analyst. Also, I have not covered all 
the libraries that exist in the world, but I have given you an overview of what they are.
< !-- >
""",
    'topics': """
< !-- >
Use this file to store your notes about various programming topics.
Topics can range from basic programming concepts to advanced topics like algorithms and 
data structures. You can use this file to jot down important points, examples, and 
explanations related to different programming topics you're studying or working on.
< !-- >
""",
    'projects': """
< !-- >
Use this file to list and describe your programming projects.
You can include details such as project name, description, technologies used, 
challenges faced, and lessons learned. This file can serve as a log of your 
programming journey and help you track your progress over time.
< !-- >
""",
    'notes': """
< !-- >
Use this file to store general programming notes and tips.
You can include code snippets, troubleshooting steps, best practices, 
and any other information that you find useful in your programming 
endeavors. This file can serve as a reference guide for you to refer 
back to when needed.
< !-- >
""",
    'readme': """
< !-- >
Use this file to provide an overview of the contents of this directory.
You can include information about the purpose of the directory, how to use 
the files inside it, and any other important details that users or collaborators 
should be aware of. This file can serve as a guide for navigating the directory 
and understanding its contents.
< !-- >
""",
    'content': """
< !-- >
Use this file to store additional content related to the programming 
language modules, topics, projects, and notes. You can use this file 
to add any extra information that doesn't fit into the other files 
but is still relevant to your programming endeavors.
< !-- >
""",
    'resources': """
< !-- >
Use this directory to store various resources related to your programming 
endeavors. Resources can include code libraries, API documentation, 
tutorials, and any other materials that you find useful in your 
programming projects. Organizing your resources in this directory 
can help you easily access them when needed.
< !-- >
""",
    'framework': """
< !-- >
Use this directory to store frameworks that you use in your programming 
projects. Frameworks can include web frameworks, testing frameworks, 
and any other frameworks that help you build and manage your projects. 
Organizing your frameworks in this directory can help you keep track 
of the frameworks you're using and their versions.
< !-- >
""",
    'design patterns': """
< !-- >
Use this directory to store information about design patterns 
that you use in your programming projects. Design patterns can 
include creational, structural, and behavioral patterns that 
help you design flexible and reusable software solutions. 
Organizing your design patterns in this directory can help 
you understand and apply them effectively in your projects.
< !-- >
""",
    'distributed systems': """
< !-- >
Use this directory to store information about distributed systems 
that you use in your programming projects. Distributed systems 
include architectures, protocols, and algorithms that enable 
computers to work together to achieve a common goal. 
Organizing your distributed systems information in this 
directory can help you design and implement distributed 
systems effectively in your projects.
< !-- >
"""
}
