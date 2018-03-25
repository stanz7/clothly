//
//  OrganizationSignInViewController.swift
//  Clothly
//
//  Created by Danny on 3/24/18.
//  Copyright © 2018 Stanley Zeng. All rights reserved.
//

import Foundation
import UIKit

class OrganizationSignInViewController: UIViewController {
    @IBOutlet weak var emailField: UITextField!
    @IBOutlet weak var passwordField: UITextField!
    @IBOutlet weak var loginButton: UIButton!
    @IBOutlet weak var registerButton: UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        emailField.layer.cornerRadius = 0
        passwordField.layer.cornerRadius = 0
    }
    
    @IBAction func signedInPressed(sender: UIButton) {
        let mainTabBarController = MainTabBarController.create(status: .org)
        if let appDelegate = UIApplication.shared.delegate as? AppDelegate {
            appDelegate.window?.rootViewController = mainTabBarController
        }
    }
    
    class func create() -> OrganizationSignInViewController {
        let storyboard = UIStoryboard(name: "Main", bundle: nil)
        let controller = storyboard.instantiateViewController(withIdentifier: "organizationSignInViewController") as! OrganizationSignInViewController
        return controller
    }
}

