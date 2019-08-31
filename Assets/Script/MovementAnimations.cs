using UnityEngine; 
using System.Collections;
using System.Collections.Generic;

public class MovementAnimations : MonoBehaviour
{
    // Transforms to act as start and end markers for the journey.
    private Vector3 startPosition;
    private Vector3 endPosition;  

    // Movement speed in units/sec.
    public float speed = 2.0F;

    // Time when the movement started.
    private float startTime;

    // Total distance between the markers.
    private float journeyLength;
    private bool journeyComplete;

    //List of moves to complete
    public List<Vector3> moves;
    private int currentMoveIdx = 0;

    //Knight Marker
    public GameObject knightMarker;

    void Start()
    {
        Vector3 firstMove = moves[currentMoveIdx];

        initJourney(transform.position + firstMove);
    }

    // Subroutine for initialization knight movement animation
    void initJourney(Vector3 endPos)
    {
        //place the marker
        placeMarker();

        //Boolean to check if the journey has been complete
        journeyComplete = false;

        //Setup markers
        startPosition = transform.position;
        endPosition = endPos;

        // Keep a note of the time the movement started.
        startTime = Time.time;

        // Calculate the journey length.
        journeyLength = Vector3.Distance(startPosition, endPosition);
    }

    void nextMove()
    {
        if (currentMoveIdx+1<moves.Count)
        {
            currentMoveIdx++;
            Vector3 nextMove = moves[currentMoveIdx];
            initJourney(transform.position + nextMove);
        }
    }

    //Places marker at visited place
    void placeMarker()
    {
        //Create a new marker
        GameObject newMarker = Instantiate(knightMarker);

        //Disable the marker 
        newMarker.SetActive(false);

        //Give the marker the knights rotation and position
        newMarker.transform.position = transform.position;
        newMarker.transform.rotation = transform.rotation;
        
        //activate the marker
        newMarker.SetActive(true);

    }

    // Follows the target position like with a spring
    void Update()
    {
        if (!journeyComplete) // only do this if the journey is in-progress
        {
            // Distance moved = time * speed.
            float distCovered = (Time.time - startTime) * speed;

            // Fraction of journey completed = current distance divided by total distance.
            float fracJourney = distCovered / journeyLength;

            // Set our position as a fraction of the distance between the markers.
            transform.position = Vector3.Lerp(startPosition, endPosition, fracJourney);
            
            //Check if the journey has been complete
            if (transform.position == endPosition)
            {
                //complete the journey
                journeyComplete = true;

                //Notify user that the journey has been complete
                Debug.Log("Journey has been complete");

                // go to the next move
                nextMove();
            }
        }
        

    }
}