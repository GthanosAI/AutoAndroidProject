from TemplateUtil import template_text


def ImageView(name, scaleType="fitXY"):
    imageview = '''<ImageView
            android:id="@+id/${name}"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:scaleType="${scaleType}" />'''

    return template_text(imageview, {
        'name': name,
        "scaleType": scaleType
    })


def TextView(name, textColor="#004c62", textSize="28px"):
    textView = """<TextView
                        android:id="@+id/${name}"
                        android:layout_width="wrap_content"
                        android:layout_height="wrap_content"
                        android:textColor="@{textColor}"
                        android:textSize="@{textSize}"
                        tools:text="demodemo" />
    """

    return template_text(textView, {
        'name': name,
        'textColor': textColor,
        'textSize': textSize
    })


def RecyclerView(name):
    recyclerView = """
     <android.support.v7.widget.RecyclerView
            android:id="@+id/${name}"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"/>
    """

    return template_text(recyclerView, {
        'name': name,
    })


def layout_header():
    head = """
    <?xml version="1.0" encoding="utf-8"?>
    <layout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools">
    """

    tail = """
        </layout>
    """
