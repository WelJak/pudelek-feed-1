package com.weljak.storageservice.webapi;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

@RestController
public class CheckerController {
    private List entries = new ArrayList();

    @PostMapping("/check")
    public ResponseEntity<CheckerResponse> checkMessage(CheckerRequest checkerRequest) {

        checkerRequest.getmessage();
        checkerRequest.createArray();
        if (entries.contains(checkerRequest.getId())) {
            CheckerResponse checkerResponse = new CheckerResponse(checkerRequest.getId(), "was already sent");
            System.out.println(entries);
            return new ResponseEntity(checkerResponse, HttpStatus.OK);
        } else {
            CheckerResponse checkerResponse = new CheckerResponse(checkerRequest.getId(), "has not been sent");
            entries.add(checkerRequest.getId());
            entries.add(Arrays.toString(checkerRequest.getArray()));
            return new ResponseEntity(checkerResponse, HttpStatus.OK);
        }

    }
}
