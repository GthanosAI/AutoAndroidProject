package ${package_name}.${sub_path};

import android.annotation.SuppressLint;
import android.content.Context;
import android.view.ViewGroup;

import ${package_name}.R;
import ${package_name}.databinding.${adapter_layout_name}Binding;
import java.util.List;
import cn.com.earth.recyclerview.CBaseRecyclerViewAdapter;
import cn.com.earth.recyclerview.JBaseDataBindingViewHolder;
import ${package_name}.${model_path}.${model_name};
import ${package_name}.${sub_path}.${page_name}Presenter


public class ${adapter_name} extends CBaseRecyclerViewAdapter<${model_name}> {
    private ${page_name}Presenter handler;

    public ${adapter_name}(List<${model_name}> list, ${page_name}Presenter presenter) {
        super(list);
        this.handler = presenter;
    }

    @Override
    protected int getViewLayoutByType(ViewGroup viewGroup, int viewType) {
        return ${adapter_layout_name};
    }

    @Override
    public void onBindViewHolder(JBaseDataBindingViewHolder holder, int position) {
        super.onBindViewHolder(holder, position);
        ${adapter_layout_name}Binding binding = (${adapter_layout_name}Binding) holder.getBinding();
        ${model_name} itemBean = list.get(position);
        Context context = binding.getRoot().getContext();
        binding.getRoot().setOnClickListener(v -> handler.handlerItemClick(itemBean));
        binding.number.setText(itemBean.getNum());
    }
}
