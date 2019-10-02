package com.weljak.storageservice.checker;

import com.weljak.storageservice.webapi.CheckerRequest;

import java.util.List;

public interface CheckerService {
    public boolean checkifmessagewassent(CheckerRequest checkerRequest, List entries);
}
