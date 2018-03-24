//
//  OrganizationCell.swift
//  Clothly
//
//  Created by Danny on 3/24/18.
//  Copyright © 2018 Stanley Zeng. All rights reserved.
//

import Foundation
import UIKit

struct Organization {
    var id: Int!
    var name: String!
    var type: String!
    var address: String!
    var city: String!
    var state: String!
    var zip: Int!
    var phoneNumber: String!
    var emailAddress: String!
}

class OrganizationCell: UITableViewCell {
    @IBOutlet weak var orgLabel: UILabel!
    @IBOutlet weak var descriptionLabel: UILabel!
    
    var organization: Organization? {
        didSet {
            if let type = organization?.type, let address = organization?.address, let city = organization?.city, let state = organization?.state, let zip = organization?.zip, let name = organization?.name, let phoneNumber = organization?.phoneNumber {
                orgLabel.text = name
                descriptionLabel.text = "\(type) • \(address) \(city), \(state) \(zip)"
            }
        }
    }
    
    override func awakeFromNib() {
        super.awakeFromNib()
        
    }
}
