//
//  LoginManager.swift
//  Clothly
//
//  Created by Danny on 3/24/18.
//  Copyright © 2018 Stanley Zeng. All rights reserved.
//

import Foundation

class LoginManager {
    static let sharedInstance = LoginManager()
    func isLoggedIn() -> Bool {
        return UserDefaults.standard.value(forKey: "donorId") != nil
    }
    
    func login(donorId: Int) {
        UserDefaults.standard.setValue("1", forKey: "donorId")
    }
    
    func getDonorId() -> Any? {
        return UserDefaults.standard.object(forKey: "donorId")
    }
    
    
    func logout() {
        UserDefaults.standard.removeObject(forKey: "donorId")
    }
}
