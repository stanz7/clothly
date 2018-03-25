//
//  SettingViewController.swift
//  Clothly
//
//  Created by Stanley Zeng on 3/24/18.
//  Copyright © 2018 Stanley Zeng. All rights reserved.
//

import Foundation
import UIKit

class SettingViewController: UIViewController {
    
    
    @IBOutlet weak var Points: UILabel!
    
    @IBOutlet weak var Donations: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        var donorId = 1
        let donorJson: [String: Any] = [
            "donorId": donorId
        ]
        DataService.sharedInstance.getDonorInfo(data: donorJson) { (data) in
            let points: String = data["points"].stringValue
            let totalDonations: String = data["totalDonations"].stringValue
            
            self.Points.text = "Total Points: \(points)"
            self.Donations.text = "Number of Donations: \(totalDonations)"
        }
    }
    
    class func create() -> SettingViewController {
        let storyboard = UIStoryboard(name: "Main", bundle: nil)
        let controller = storyboard.instantiateViewController(withIdentifier: "settingViewController") as! SettingViewController
        
        let _ = controller.view
        
        return controller
    }
}

