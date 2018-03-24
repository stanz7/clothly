//
//  DataService.swift
//  Clothly
//
//  Created by Danny on 3/24/18.
//  Copyright © 2018 Stanley Zeng. All rights reserved.
//

import Foundation
import Alamofire
import SwiftyJSON

class DataService {
    static let sharedInstance = DataService()
    func getOrganizations(complete:@escaping (_ data: JSON) -> Void) {
        
        var returnData: JSON? = nil

        Alamofire.request(BASE_URL + "getOrganizations", method: .get).responseJSON { (response) in
            switch response.result {
            case .success(let data):
                let jsonData = JSON(response.result.value!)
                returnData = jsonData
                complete(returnData!)
            case .failure(let error):
                print(error)
            }
        }
    }
    func createDonation(data: [String: Any]) {
        Alamofire.request(BASE_URL + "createDonation", method: .post, parameters: data, encoding: JSONEncoding.default, headers: [:]).responseString { (response) in
            switch response.result {
            case .success(let data):
                print(data)
            case .failure(let error):
                print(error)
            }
        }
    }
}
