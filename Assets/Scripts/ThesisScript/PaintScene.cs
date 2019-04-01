﻿using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEngine;
using UnityEngine.UI;

public class PaintScene : MonoBehaviour {
    [SerializeField] private GameObject paintButton;
    [SerializeField] private GameObject backButton;
    [SerializeField] private Image image;
    [SerializeField] private Canvas myCanvas;
    private Sprite screenshot;
    private string path;

    // Use this for initialization
    void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
            
        
    }

    public void runPaint() {
        StartCoroutine(Paint());
    }

    private IEnumerator Paint() {
        myCanvas.enabled = false;
        screenShot();
        yield return new WaitUntil(() => File.Exists(path) == true);
        showScreenShot();
    }

    private void screenShot() {
        Debug.Log(Application.persistentDataPath);
        path = Application.persistentDataPath + "/UnalteredScene.png";
        //path = "D:/School/GAME/AR-Impress-Me/UnalteredScene.png";
        ScreenCapture.CaptureScreenshot("UnalteredScene.png");
        //ScreenCapture.CaptureScreenshot(path);
        Debug.Log(path);
    }

    private void showScreenShot() {
        Debug.Log("1");
        DisplayImage(path);
        image.enabled = true;
        paintButton.SetActive(false);
        backButton.SetActive(true);
        myCanvas.enabled = true;
        Debug.Log("2");
    }

    private void DisplayImage(string path) {
        if (System.IO.File.Exists(path)) {
            Debug.Log("3");
            byte[] bytes = System.IO.File.ReadAllBytes(path);
            Texture2D texture = new Texture2D(1, 1);
            texture.LoadImage(bytes);
            Sprite sprite = Sprite.Create(texture, new Rect(0, 0, texture.width, texture.height), new Vector2(0.5f, 0.5f), 100);
            image.sprite = sprite;
            screenshot = sprite;
            Debug.Log("4");
        }
    }

    public void back() {
        File.Delete(path);
        image.enabled = false;
        backButton.SetActive(false);
        paintButton.SetActive(true);
    }
}
