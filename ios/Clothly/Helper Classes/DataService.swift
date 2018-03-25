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
    
    func getPendingDonations(data: [String:Any], complete:@escaping (_ data: JSON) -> Void) {
        var returnData: JSON? = nil
        
        Alamofire.request(BASE_URL + "getPendingDonations", method: .post, parameters: data, encoding: JSONEncoding.default, headers: [:]).responseJSON { (response) in
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
    
    func getPastDonations(data: [String:Any], complete:@escaping (_ data: JSON) -> Void) {
        var returnData: JSON? = nil
        
        Alamofire.request(BASE_URL + "getPastDonations", method: .post, parameters: data, encoding: JSONEncoding.default, headers: [:]).responseJSON { (response) in
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
    
    func orgGetPastDonations(data: [String:Any], complete:@escaping (_ data: JSON) -> Void) {
        var returnData: JSON? = nil
        
        Alamofire.request(BASE_URL + "getPastDonors", method: .post, parameters: data, encoding: JSONEncoding.default, headers: [:]).responseJSON { (response) in
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
    
    func orgGetPendingDonations(data: [String:Any], complete:@escaping (_ data: JSON) -> Void) {
        var returnData: JSON? = nil
        
        Alamofire.request(BASE_URL + "getDonors", method: .post, parameters: data, encoding: JSONEncoding.default, headers: [:]).responseJSON { (response) in
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
    
}
