//
//  AffiliationViewController.swift
//  Clothly
//
//  Created by Danny on 3/24/18.
//  Copyright © 2018 Stanley Zeng. All rights reserved.
//

import Foundation
import UIKit

enum AuthenticationStatus {
    case login
    case register
}

class AffiliationViewController: UIViewController {
    
    var status: AuthenticationStatus!
    
    @IBOutlet weak var donorButton: UIButton!
    @IBOutlet weak var organizationButton: UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
    }
    
    @IBAction func donorPressed(sender: UIButton) {
        if let appDelegate = UIApplication.shared.delegate as? AppDelegate {
            appDelegate.status = .donor
        }
        switch status {
        case .login:
            let donorSignInViewController = DonorSignInViewController.create()
            self.navigationController?.pushViewController(donorSignInViewController, animated: true)
        case .register:
            return
        default:
            break
        }
    }
    
    @IBAction func organizationPressed(sender: UIButton) {
        if let appDelegate = UIApplication.shared.delegate as? AppDelegate {
            appDelegate.status = .org
        }
        switch status {
        case .login:
            let organizationViewController = OrganizationSignInViewController.create()
            self.navigationController?.pushViewController(organizationViewController, animated: true)
        case .register:
            return
        default:
            break
        }
    }
    
    class func create() -> AffiliationViewController {
        let storyboard = UIStoryboard(name: "Main", bundle: nil)
        let controller = storyboard.instantiateViewController(withIdentifier: "affiliationViewController") as! AffiliationViewController
        return controller
    }
}
