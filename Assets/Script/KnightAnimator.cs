using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class KnightAnimator : MonoBehaviour
{

    private float x_offset = 3.0f;
    private float y_offset = 3.0f;

    // Start is called before the first frame update
    void Start()
    {
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    void moveRight()
    {
        Vector3 startPosition = transform.position;
        startPosition.x += x_offset;
        transform.position = startPosition;
    }

    void moveLeft()
    {
        Vector3 startPosition = transform.position;
        startPosition.x -= x_offset;
        transform.position = startPosition;
    }

    void moveUp()
    {
        Vector3 startPosition = transform.position;
        startPosition.z += y_offset;
        transform.position = startPosition;
    }
}
