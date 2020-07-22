from django.contrib.auth.models import User

from rest_framework import serializers

from .models import product, gender, brand, category, size, orderMaster, orderDetail, cartItem, orderStatus


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name',
                  'last_name', 'email', 'password', 'password2']

    def save(self):
        account = User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError(
                {'password': 'Password must match'})

        account.set_password(password)
        account.save()
        return account


class ProductSerializer(serializers.ModelSerializer):
    # gender = serializers.HyperlinkedRelatedField(many=True, view_name='gender-list', read_only=True)
    # gender = serializers.HyperlinkedIdentityField(view_name="gender-list")

    class Meta:
        model = product
        fields = ['id', 'image', 'name', 'description',
                  'price', 'gender', 'brand', 'category']
        depth = 1


class GenderSerializer(serializers.ModelSerializer):

    class Meta:
        model = gender
        fields = ['id', 'gender']


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = brand
        fields = ['id', 'name']


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = category
        fields = ['id', 'name']


class SizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = size
        fields = ['id', 'size']


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = orderStatus
        fields = ['id', 'name']


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
   # user = UserSerializer(read_only=True, many=True)
    statusname = serializers.CharField(source='status.name')
    #status = StatusSerializer(read_only=True, many=True)
    class Meta:
        model = orderMaster
        fields = ['id', 'user', 'amount', 'timestamp', 'status', 'address', 'statusname']
        #depth = 1
        def save(self):
            order = orderMaster(
                user=self.user,
                amount=self.validated_data['amount'],
            )
            order.save()
            cart = cartItem.objects.filter(user=self.user)
            detail = orderDetail(
                order=order,
                product=x.item,
                price=x.item.price,
                Shoesize=x.Shoesize
            )
            detail.save()

            return order

        def update(self, instance, validatedData):
            sid = validatedData.get['status']
            ID = self.validated_data['status']
            print(instance.status)
            #master = orderMaster.objects.get(id=id)
            s = orderStatus.objects.get(id=sid)
            print(s)
            instance.status = orderStatus.objects.get(id=ID)
            instance.save()

            return instance


class OrderDetailSerializer(serializers.ModelSerializer):
    # order = serializers.ReadOnlyField(source='order.id')
    class Meta:
        model = orderDetail
        fields = ['id', 'order', 'product', 'price', 'Shoesize']
        #depth = 1

        def save(self):

            #cart = cartItem.objects.filter(user=self.user)
            # for x in cart:
            order = self.validated_data['order'],
            detail = orderDetail(
                order=orderDetail.objects.get(id=order),
                product=self.product,
                price=self.price,
                Shoesize=self.Shoesize
            )
            detail.save()

            return detail


class CartItemSerializer(serializers.ModelSerializer):
    # order = serializers.ReadOnlyField(source='order.id')
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = cartItem
        fields = ['id', 'user', 'item', 'Shoesize']

        def save(self):
            ID = self.validated_data['item']

            addItem = cartItem(
                user=self.user,
                item=ID,
                Shoesize=self.validated_data['Shoesize']
            )
            addItem.save()
            return addItem
