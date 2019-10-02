package com.weljak.storageservice.webapi;

import com.weljak.storageservice.checker.CheckerService;
import com.weljak.storageservice.checker.MockCheckerService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

@RestController
public class CheckerController {
    CheckerService checkerService = new MockCheckerService();
    private List entries = new ArrayList();

    @PostMapping("/check")
    public ResponseEntity<CheckerResponse> checkMessage(CheckerRequest checkerRequest) {
        System.out.println(entries);
        return new ResponseEntity(checkerService.checkifmessagewassent(checkerRequest,entries), HttpStatus.OK);
    }
}