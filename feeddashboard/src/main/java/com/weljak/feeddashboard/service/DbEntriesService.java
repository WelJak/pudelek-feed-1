package com.weljak.feeddashboard.service;

import com.google.gson.Gson;
import com.google.gson.JsonArray;
import com.google.gson.JsonObject;
import com.google.gson.reflect.TypeToken;
import com.weljak.feeddashboard.domain.News;
import lombok.RequiredArgsConstructor;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClientBuilder;
import org.apache.http.util.EntityUtils;
import org.springframework.stereotype.Service;

import java.io.IOException;
import java.util.List;

@Service
@RequiredArgsConstructor
public class DbEntriesService implements EntriesService {
    Gson gson = new Gson();
    private final String URL = "http://localhost:8080/messages/all";

    @Override
    public List<News> listAllEntries() {
        try {
            HttpGet request = new HttpGet(URL);
            CloseableHttpClient client = HttpClientBuilder.create().build();
            CloseableHttpResponse response = client.execute(request);
            String result = EntityUtils.toString(response.getEntity());
            JsonArray arr = gson.fromJson(result, JsonObject.class).getAsJsonArray("listOfNews");
            List<News> entries = gson.fromJson(arr, new TypeToken<List<News>>() {
            }.getType());
            return entries;
        } catch (IOException ioe) {
            ioe.printStackTrace();
            return null;
        }
    }
}
