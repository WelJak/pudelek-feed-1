package com.weljak.storageservice.checker;

import com.weljak.storageservice.webapi.CheckerRequest;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class MockCheckerService implements CheckerService {
    private List entries = new ArrayList();
    @Override
    public boolean checkifmessagewassent(CheckerRequest checkerRequest) {
        if (entries.contains(checkerRequest)){
            System.out.println("message was already sent");
            System.out.println(checkerRequest);
            return true;
        }else{
            System.out.println("message has not been sent yet");
            entries.add(checkerRequest);
            System.out.println(entries);
            return false;
        }

    }
}
