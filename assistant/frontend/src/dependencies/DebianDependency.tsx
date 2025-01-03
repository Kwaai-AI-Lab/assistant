// DebianDependency.tsx
import { Datagrid, TextField } from 'react-admin';

export const DebianDependency = (props: { dependencies: any }) => {
    return (
        <Datagrid data={props.dependencies} sort={{ field: 'name', order: 'ASC' }}>
            <TextField source="name" />
        </Datagrid>
    );
};
