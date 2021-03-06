//
//  DonorSignInViewController.swift
//  Clothly
//
//  Created by Danny on 3/24/18.
//  Copyright © 2018 Stanley Zeng. All rights reserved.
//

import Foundation
import UIKit
import Alamofire

class DonorSignInViewController: UIViewController {
    @IBOutlet weak var emailField: UITextField!
    @IBOutlet weak var passwordField: UITextField!
    @IBOutlet weak var loginButton: UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        emailField.layer.cornerRadius = 0
        passwordField.layer.cornerRadius = 0
    }
    
    var parameters: [String: AnyObject] = [:]
    
    @IBAction func signInPressed(sender: UIButton) {
        let emailAddress = emailField.text
        let password = passwordField.text
        parameters["emailAddress"] = emailAddress as AnyObject
        parameters["password"] = password as AnyObject
        // 54.175.31.104/api/donorLogin
//        Alamofire.request(BASE_URL+"donorLogin", method: .post, parameters: parameters, encoding: JSONEncoding.default, headers: nil).responseString { (response) in
//            if (response.result.isSuccess) {
//                switch response.result {
//                case .failure(let error):
//                    return
//                case .success(let data):
//                    guard let json = data as? [String: AnyObject] else {
//                        return
//                    }
//                    print(json)
//                }
//            } else {
//                print("error")
//            }
//        }
//        let organizationPickController = OrganizationPickViewController.create()
//        self.navigationController?.pushViewController(organizationPickController, animated: true)
//
        let mainTabBarController = MainTabBarController.create(status: .donor)
        if let appDelegate = UIApplication.shared.delegate as? AppDelegate {
            appDelegate.window?.rootViewController = mainTabBarController
        }
        
    }
    
    class func create() -> DonorSignInViewController {
        let storyboard = UIStoryboard(name: "Main", bundle: nil)
        let controller = storyboard.instantiateViewController(withIdentifier: "donorSignInViewController") as! DonorSignInViewController
        return controller
    }
}
