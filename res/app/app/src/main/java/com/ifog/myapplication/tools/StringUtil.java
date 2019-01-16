package ${package_name}.tools;

/**
 * 介绍:
 * 作者: jacky
 * 时间: 2018/12/12 10:16 AM
 */
public class StringUtil {
    public static String toConvert(Object... objects) {
        StringBuilder builder = new StringBuilder();
        for (Object o : objects) {
            builder.append(o);
        }

        return builder.toString();
    }
}
