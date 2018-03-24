//
//  ViewController.swift
//  Clothly
//
//  Created by Danny Lin on 3/24/18.
//  Copyright © 2018 Danny Lin. All rights reserved.
//

import UIKit

class MainViewController: UIViewController {
    
    @IBOutlet weak var loginButton: UIButton!
    @IBOutlet weak var registerButton: UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        loginButton.layer.cornerRadius = 5
        registerButton.layer.cornerRadius = 5
        // Do any additional setup after loading the view, typically from a nib.
    }
    
    @IBAction func buttonPressed(sender: UIButton) {
        let status: AuthenticationStatus = sender.tag == 1 ? .register : .login
        let affiliationViewController = AffiliationViewController.create()
        affiliationViewController.status = status
        self.navigationController?.pushViewController(affiliationViewController, animated: true)
    }
    
    class func create() -> MainViewController {
        let storyboard = UIStoryboard(name: "Main", bundle: nil)
        let controller = storyboard.instantiateViewController(withIdentifier: "mainViewController") as! MainViewController
        return controller
    }

}

