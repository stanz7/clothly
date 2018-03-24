//
//  OrganizationPickViewController.swift
//  Clothly
//
//  Created by Danny on 3/24/18.
//  Copyright © 2018 Stanley Zeng. All rights reserved.
//

import Foundation
import UIKit

class OrganizationPickViewController: UIViewController {
    var data: Array<Dictionary<String, Any>> = [["orgName": "The Salvation Army", "orgId": 1, "orgType": "Salvation Army", "address": "2550 Benson Ave", "city": "Brooklyn", "state": "NY", "zip": 11214, "emailAddress": "danny.lin@nyu.edu", "phoneNumber": "9173990398"], ["orgName": "George's Church", "orgId": 2, "orgType": "Local Church", "address": "7214 18th Avenue", "city": "Brooklyn", "state": "NY", "zip": 11204, "emailAddress": "george.church@gmail.com", "phoneNumber": "7182343722"]]
    
    @IBOutlet weak var tableView: UITableView!
    @IBOutlet weak var searchBar: UISearchBar!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        tableView.estimatedRowHeight = 75
        tableView.rowHeight = UITableViewAutomaticDimension
    }
    
    class func create() -> OrganizationPickViewController {
        let storyboard = UIStoryboard(name: "Main", bundle: nil)
        let controller = storyboard.instantiateViewController(withIdentifier: "organizationPickViewController") as! OrganizationPickViewController
        return controller
    }
}

extension OrganizationPickViewController: UITableViewDelegate, UITableViewDataSource {
    func numberOfSections(in tableView: UITableView) -> Int {
        return 1
    }
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return data.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        guard let cell = tableView.dequeueReusableCell(withIdentifier: "OrganizationCell") as? OrganizationCell else {
            return UITableViewCell()
        }
        let cellData = data[indexPath.row]
        var organization = Organization()
        organization.name = cellData["orgName"] as? String
        organization.type = cellData["orgType"] as? String
        organization.id = cellData["orgId"] as? Int
        organization.address = cellData["address"] as? String
        organization.city = cellData["city"] as? String
        organization.state = cellData["state"] as? String
        organization.zip = cellData["zip"] as? Int
        organization.phoneNumber = cellData["phoneNumber"] as? String
        organization.emailAddress = cellData["emailAddress"] as? String
        cell.organization = organization
        
        return cell
    }
    
    func tableView(_ tableView: UITableView, heightForRowAt indexPath: IndexPath) -> CGFloat {
        return 75
    }
}
