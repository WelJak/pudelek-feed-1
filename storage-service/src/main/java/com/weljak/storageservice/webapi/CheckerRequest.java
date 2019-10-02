package com.weljak.storageservice.webapi;

import lombok.Data;
import lombok.Value;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

@Value
public class CheckerRequest {
    private String id;
    private String date;
    private String title;
    private String description;
    private List <String> tags;
    private String link;

}
