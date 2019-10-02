package com.weljak.storageservice.webapi;

import com.weljak.storageservice.checker.CheckerService;
import com.weljak.storageservice.checker.MockCheckerService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class CheckerController {
    CheckerService checkerService = new MockCheckerService();

    @PostMapping("/check")
    public ResponseEntity<CheckerResponse> checkMessage(@RequestBody CheckerRequest checkerRequest) {
        return new ResponseEntity(checkerService.checkifmessagewassent(checkerRequest), HttpStatus.OK);
    }
}