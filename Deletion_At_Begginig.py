
import Main_ll as ll
import __main as d
import turtle
import time
from turtle import *

screen=None
llist = [5, 2, 3, 4, 1]

# Function for Deletion in Linked list at first position
def delete_At_Beginning(screen ):
    bgcol="#B9F3FC"
    screen.bgcolor(bgcol)
    d.createObject('db_Null', screen,  visibility=False , speed=0, color="black")
    d.createObject('db_title', screen, visibility=False, speed=0, color="black")
    d.createObject('db_steps', screen, visibility=False, speed=0, color="black")

    d.createObject('db_nodes', screen, visibility=False, speed=0, color="black")
    d.createObject('db_links', screen, visibility=False, speed=0, color="black")

    d.createObject('db_newheadarrow', screen, visibility=False, speed=0, color="black")

    d.createObject('db_head', screen, visibility=False, speed=0, color="black")
    d.createObject('db_tail', screen, visibility=False, speed=0, color="black")
    d.createObject('db_temp', screen, visibility=False, speed=0, color="black")

    d.createObject('db_head1', screen, visibility=False, speed=0, color="black")
    d.createObject('db_tail1', screen, visibility=False, speed=0, color="black")
    d.createObject('db_newhead', screen, visibility=False, speed=0, color="black")
    d.createObject('db_newtail', screen, visibility=False, speed=0, color="black")

    d.createObject('db_linkclear', screen, visibility=False, speed=0, color="black")

    db_temp = d.db_temp
    db_nodes = d.db_nodes
    db_newheadarrow = d.db_newheadarrow
    db_links = d.db_links

    db_head = d.db_head
    db_tail = d.db_tail
    db_head1 = d.db_head1
    db_tail1 = d.db_tail1
    db_linkclear = d.db_linkclear
    db_newhead = d.db_newhead
    db_newtail = d.db_newtail
    db_title = d.db_title
    db_steps = d.db_steps
    db_Null = d.db_Null

    db_title.up()
    db_steps.up()
    db_title.goto(d.horizontal + 50, d.vertical)
    db_title.write("Linked List:", font=("normal", 12, "bold"))

    d.setPosition(100, 300)
    ll.LinkedList(db_nodes, db_links, db_head, db_tail, llist, length=90, width=100 , null=db_Null)

    d.setPosition(0, 200)
    db_title.goto(d.horizontal - 50, d.vertical)
    db_title.write("Deletion At Beginning in LL:", font=("normal", 12, "bold"))
    ll.LinkedList(db_nodes, db_links, db_head1, db_tail1, llist, yPos=250, length=90, width=100, clear="no" , null=db_Null)

    db_steps.goto(d.horizontal + 250, d.vertical - 350)
    db_steps.write("Step 1: Make temp = head", font=("normal", 6, "bold"))
    time.sleep(1.2)

    ll.head(db_temp, x=ll.arrowPos[0][0], y=ll.arrowPos[0][1] + (ll.nodewid * 0.81), col="red", text="temp")
    time.sleep(1.2)

    ll.head(db_newheadarrow, pos=1, x=ll.arrowPos[1][0], y=ll.arrowPos[1][1] + (ll.nodewid * 0.81), col="red", text="head")
    db_head1.clear()
    db_steps.goto(db_steps.xcor(), db_steps.ycor() - 50)
    db_steps.write("Step 2: Make temp -> next link free", font=("normal", 6, "bold"))
    time.sleep(1.2)
    ll.link(db_linkclear, xcor=ll.arrowPos[0][0] + ll.nodelen * 0.799, ycor=ll.arrowPos[0][1] + ll.nodewid * 0.25,
            color="#B9F3FC", size=7)
    db_head.up()

    db_head.goto(ll.arrowPos[0][0] - ll.nodelen * 0.6, ll.arrowPos[0][1] - ll.nodewid * 0.30)
    db_steps.goto(db_steps.xcor(), db_steps.ycor() - 50)
    db_steps.write("Step 3: Make free Node which temp is indicating", font=("normal", 6, "bold"))
    db_temp.clear()
    db_head.fillcolor("#B9F3FC")
    db_head.begin_fill()
    db_head.goto(db_head.xcor(), db_head.ycor() + ll.nodewid * 1.5)
    db_head.goto(db_head.xcor() + ll.nodelen * 2, db_head.ycor())
    db_head.goto(db_head.xcor(), db_head.ycor() - ll.nodewid * 1.5)
    db_head.goto(db_head.xcor() - ll.nodelen * 2, db_head.ycor())
    db_head.end_fill()

    ll.arrowPos.clear()
    d.setPosition(0, 700)
    db_title.goto(d.horizontal - 50, d.vertical)
    db_title.write("After Deletion in LL:", font=("normal", 12, "bold"))
    llist.pop(0)
    ll.LinkedList(db_nodes, db_links, db_newhead, db_newtail, llist, yPos=250, length=90, width=100 , null = db_Null )


# Function to handle the window closing event
def delete_beg(screen):
    try:
        d.setPosition( )
        delete_At_Beginning(screen)
        time.sleep(5)
        d.setPosition( )
        #d.screen.bye()  # Close the turtle window
    except turtle.Terminator:
        pass  # Catch the Terminator error and do nothing
    except Exception as e:
        pass
        print("An error occurred:", str(e))  # Handle any other exception and print an error message


# Main Driver Program
# Set the close_window function to handle the window closing event
#d.screen.onkey(close_window_delete_at_beg_LL, "q")
#d.screen.listen()
delete_beg(screen)

