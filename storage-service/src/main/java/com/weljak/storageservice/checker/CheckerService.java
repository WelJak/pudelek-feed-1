package com.weljak.storageservice.checker;

import com.weljak.storageservice.webapi.CheckerRequest;

public interface CheckerService {
    public boolean checkifmessagewassent(CheckerRequest checkerRequest);
}
