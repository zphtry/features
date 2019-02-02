ClassDecorator = <TFunction extends Function>(target: TFunction) => TFunction | void;

PropertyDecorator = (target: Object, propertyKey: string | symbol) => void;

MethodDecorator = <T>(target: Object, propertyKey: string | symbol, descriptor: TypedPropertyDescriptor<T>) => TypedPropertyDescriptor<T> | void;

ParameterDecorator = (target: Object, propertyKey: string | symbol, parameterIndex: number) => void;