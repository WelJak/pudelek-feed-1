package com.weljak.storageservice.checker;

import com.weljak.storageservice.webapi.CheckerRequest;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
public class MockCheckerService implements CheckerService {
    public List<String> entries = new ArrayList<>();


    @Override
    public boolean checkIfMessageWasSent(CheckerRequest checkerRequest) {
        if (entries.contains(checkerRequest.getEntryid())) {
            System.out.println("message was already sent");
            System.out.println(entries);
            return true;
        } else {
            System.out.println("message has not been sent yet");
            entries.add(checkerRequest.getEntryid());
            System.out.println(entries);
            return false;
        }

    }
}
