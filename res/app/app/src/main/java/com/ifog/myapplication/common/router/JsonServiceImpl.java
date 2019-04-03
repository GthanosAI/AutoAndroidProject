package com.ifog.demo.common.router;

import android.content.Context;

import com.alibaba.android.arouter.facade.annotation.Route;
import com.alibaba.android.arouter.facade.service.SerializationService;
import com.google.gson.Gson;

import java.lang.reflect.Type;

@Route(path = "/base/jsonService")
public class JsonServiceImpl implements SerializationService {

    private Gson gson;

    public JsonServiceImpl() {
    }

    @Override
    public <T> T json2Object(String json, Class<T> clazz) {
        return gson.fromJson(json, clazz);
    }

    @Override
    public String object2Json(Object instance) {
        return gson.toJson(instance);
    }

    @Override
    public <T> T parseObject(String input, Type clazz) {
        return gson.fromJson(input, clazz);
    }

    @Override
    public void init(Context context) {
        gson = new Gson();
    }
}
