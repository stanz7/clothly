//
//  OrganizationPickViewController.swift
//  Clothly
//
//  Created by Danny on 3/24/18.
//  Copyright © 2018 Stanley Zeng. All rights reserved.
//

import Foundation
import UIKit
import SwiftyJSON

class OrganizationPickViewController: UIViewController {
    var dataSource: [JSON] = [] {
        didSet {
            self.tableView.reloadData()
        }
    }
    
    @IBOutlet weak var tableView: UITableView!
    @IBOutlet weak var searchBar: UISearchBar!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        tableView.estimatedRowHeight = 75
        tableView.rowHeight = UITableViewAutomaticDimension
    }
    
    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        DataService.sharedInstance.getOrganizations { (data) in
            self.dataSource = data["data"].array!
        }
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
        return self.dataSource.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        guard let cell = tableView.dequeueReusableCell(withIdentifier: "OrganizationCell") as? OrganizationCell else {
            return UITableViewCell()
        }
        let cellData = self.dataSource[indexPath.row]
        var organization = Organization()
        organization.name = cellData["orgName"].stringValue
        organization.type = cellData["orgType"].stringValue
        organization.id = cellData["orgId"].intValue
        organization.address = cellData["address"].stringValue
        organization.city = cellData["city"].stringValue
        organization.state = cellData["state"].stringValue
        organization.zip = cellData["zip"].intValue
        organization.phoneNumber = cellData["phoneNumber"].stringValue
        organization.emailAddress = cellData["emailAddress"].stringValue
        cell.organization = organization
        
        return cell
    }
    
    func tableView(_ tableView: UITableView, heightForRowAt indexPath: IndexPath) -> CGFloat {
        return 75
    }
}
