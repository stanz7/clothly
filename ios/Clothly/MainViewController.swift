//
//  ViewController.swift
//  Clothly
//
//  Created by Stanley Zeng on 3/24/18.
//  Copyright © 2018 Stanley Zeng. All rights reserved.
//

import UIKit

class MainViewController: UIViewController {
    
    
    @IBAction func SignUpPressed(_ sender: AnyObject) {
        self.performSegue(withIdentifier: "signUp", sender: self)
    }
    @IBAction func LoginPressed(_ sender: AnyObject) {
        self.performSegue(withIdentifier: "Login", sender: self)
    }
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

