//
//  DonationViewController.swift
//  Clothly
//
//  Created by Danny on 3/24/18.
//  Copyright © 2018 Stanley Zeng. All rights reserved.
//

import Foundation
import UIKit
import SwiftyJSON

class DonationViewController: UIViewController {
    
    var organization: Organization! {
        didSet {
            orgLabel.text = organization.name!
        }
    }
    
    let pickerData: [String] = ["Tops", "Bottoms", "Shoes", "Overalls", "Accessories", "Other"]
    var selectedRow: Int = 0
    var currentQuantity = 0
    
    @IBOutlet weak var orgLabel: UILabel!
    @IBOutlet weak var typePicker: UIPickerView!
    @IBOutlet weak var instructionsTextView: UITextView!
    @IBOutlet weak var datePicker: UIDatePicker!
    @IBOutlet weak var quantitySlider: UISlider!
    @IBOutlet weak var quantityLabel: UILabel!
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
    }
    
    class func create() -> DonationViewController {
        let storyboard = UIStoryboard(name: "Main", bundle: nil)
        let controller = storyboard.instantiateViewController(withIdentifier: "donationViewController") as! DonationViewController
        let _ = controller.view
        return controller
    }
    
    @IBAction func submitPressed(sender: UIButton) {
        let dateFormatter = DateFormatter()
        dateFormatter.dateFormat = "yyyy-MM-dd hh:mm:ss"
        var date = datePicker.date
        var formattedDate = dateFormatter.string(from: date)
        
        let json: [String: Any] = [
            "orgName": organization.name,
            "type": pickerData[selectedRow],
            "instructions": instructionsTextView.text,
            "orgId": organization.id,
            "quantity": currentQuantity,
            "pickUpDate": formattedDate,
            "donorId": 1
        ]
        DataService.sharedInstance.createDonation(data: json)
    }
    
    @IBAction func sliderValueChanged(sender: UISlider) {
        quantityLabel.text = "\(Int(sender.value))"
        currentQuantity = Int(sender.value)
    }
}

extension DonationViewController: UIPickerViewDelegate, UIPickerViewDataSource {
    func numberOfComponents(in pickerView: UIPickerView) -> Int {
        return 1
    }
    
    func pickerView(_ pickerView: UIPickerView, numberOfRowsInComponent component: Int) -> Int {
        return pickerData.count
    }
    
    func pickerView(_ pickerView: UIPickerView, titleForRow row: Int, forComponent component: Int) -> String? {
        return pickerData[row]
    }
    
    func pickerView(_ pickerView: UIPickerView, didSelectRow row: Int, inComponent component: Int) {
        self.selectedRow = component
    }
}
