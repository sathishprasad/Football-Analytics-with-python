# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 22:56:58 2020

@author: Sathish
"""
from matplotlib.patches import Arc
import matplotlib.pyplot as plt
import matplotlib

def createPitch(length,width,linecolour,pitchcolour):
    #Create figure
    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)

    #Pitch Outline & Centre Line
    plt.plot([0,0],[0,width], color=linecolour)
    plt.plot([0,length],[width,width], color=linecolour)
    plt.plot([length,length],[width,0], color=linecolour)
    plt.plot([length,0],[0,0], color=linecolour)
    plt.plot([length/2,length/2],[0,width], color=linecolour)

    #Left Penalty Area
    ax.plot([18 ,18],[(width/2 +18),(width/2-18)],color=linecolour)
    ax.plot([0,18],[(width/2 +18),(width/2 +18)],color=linecolour)
    ax.plot([18,0],[(width/2 -18),(width/2 -18)],color=linecolour)
        

    #Right Penalty Area
    ax.plot([(length-18),length],[(width/2 +18),(width/2 +18)],color=linecolour, zorder=2)
    ax.plot([(length-18), (length-18)],[(width/2 +18),(width/2-18)],color=linecolour, zorder=2)
    ax.plot([(length-18),length],[(width/2 -18),(width/2 -18)],color=linecolour, zorder=2)
    
    #Left 6-yard Box
    ax.plot([0,6],[(width/2+7.32/2+6),(width/2+7.32/2+6)],color=linecolour)
    ax.plot([6,6],[(width/2+7.32/2+6),(width/2-7.32/2-6)],color=linecolour)
    ax.plot([6,0],[(width/2-7.32/2-6),(width/2-7.32/2-6)],color=linecolour)
    
    
    #Right 6-yard Box
    ax.plot([length,length-6],[(width/2+7.32/2+6),(width/2+7.32/2+6)],color=linecolour)
    ax.plot([length-6,length-6],[(width/2+7.32/2+6),width/2-7.32/2-6],color=linecolour)
    ax.plot([length-6,length],[(width/2-7.32/2-6),width/2-7.32/2-6],color=linecolour)
    
    #Prepare Circles; 10 yards distance. penalty on 12 yards
    centreCircle = plt.Circle((length/2,width/2),10,color=linecolour,fill=False)
    centreSpot = plt.Circle((length/2,width/2),0.4,color=linecolour)
    leftPenSpot = plt.Circle((12,width/2),0.4,color=linecolour)
    rightPenSpot = plt.Circle((length-12,width/2),0.4,color=linecolour)
    

    
    #Prepare Arcs
    leftArc = Arc((11,width/2),height=20,width=20,angle=0,theta1=312,theta2=48,color=linecolour)
    rightArc = Arc((length-11,width/2),height=20,width=20,angle=0,theta1=130,theta2=230,color=linecolour)
        


    
    #Remove axis
    plt.axis('off')
    
    rect1 = matplotlib.patches.Rectangle((-3,-3), length+6, length+12, color=pitchcolour)
    
    #Display Circles and Arcs
    ax.add_patch(rect1)
    ax.add_patch(centreCircle)
    ax.add_patch(centreSpot)
    ax.add_patch(leftPenSpot)
    ax.add_patch(rightPenSpot)
    ax.add_patch(leftArc)
    ax.add_patch(rightArc)
    
    plt.show()
    
    return fig,ax






   
