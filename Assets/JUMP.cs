using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class JUMP : MonoBehaviour
{
    protected float Animation;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKey("space"))
        {

            Animation += Time.deltaTime;
            Animation = Animation % 1f;
            transform.position = MathParabola.Parabola(BossController.rb.position, new Vector3(BossController.rb.position.x, BossController.rb.position.y, BossController.rb.position.z + 5f), 5f, Animation / 1f);
     
        }
        
    }
}
