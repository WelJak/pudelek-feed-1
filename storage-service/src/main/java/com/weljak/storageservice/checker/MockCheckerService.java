package com.weljak.storageservice.checker;

import com.weljak.storageservice.webapi.CheckerRequest;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class MockCheckerService implements CheckerService {
    @Override
    public boolean checkifmessagewassent(CheckerRequest checkerRequest, List entries) {
        checkerRequest.getmessage();
        checkerRequest.create_output_part();
        if (entries.contains(Arrays.toString(checkerRequest.getEntry()))){
            System.out.println("message was already sent");
            System.out.println(Arrays.toString(checkerRequest.getEntry()));
            return true;
        }else{
            System.out.println("message has not been sent yet");
            entries.add(Arrays.toString(checkerRequest.getEntry()));
            return false;
        }

    }
}
